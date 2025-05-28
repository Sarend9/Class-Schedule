from LLM import llm
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import MessagesState, StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from AddEventTool import add_event
from FindEventsByDateTool import find_events_by_date
from datetime import datetime

graph_builder = StateGraph(MessagesState)

tools = [add_event, find_events_by_date]

llm_with_tools = llm.bind_tools(tools)

def chatbot(state: MessagesState):
    system_prompt = """Ты электронный планировщик.
        Если пользователь не указал время, значит его интересует точность до даты. В этом случае не нужно уточнять время.
        Если событие пересекается с другим ранее запланированным событием сообщи об этом и сохраняй только после подтверждения пользователя.
    """

    messages = state["messages"]
    if len(messages)==1:
        messages = [SystemMessage(content=system_prompt), *messages]

    messages = [*messages, SystemMessage(content=f'Текущее точное время в формате %Y-%m-%d %H:%M:%S - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')]
    return {"messages": [llm_with_tools.invoke(messages)]}

graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "chatbot")

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")

memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

printed_value_ids = set()  # Для отслеживания уже выведенных сообщений

def print_stream_events(events):
    for event in events:
        if "messages" in event:
            for value in event["messages"]:
                value_id = getattr(value, "id", None)
                if value_id and value_id not in printed_value_ids:
                    value.pretty_print()
                    printed_value_ids.add(value_id)


config = {"configurable": {"thread_id": "1"}}

while True:
    user_input = input("User: ")

    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break

    events = graph.stream(
        {"messages": [HumanMessage(content=user_input)]},
        config,
        stream_mode="values",
    )

    print_stream_events(events)
