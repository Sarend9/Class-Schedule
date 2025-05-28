import httpx
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import configparser

# Создаём парсер и читаем файл
config = configparser.ConfigParser()
config.read('config.ini')

# Получаем параметры из секции [llm]
llm_config = config['llm']
base_url = llm_config.get('base_url')
api_key = llm_config.get('api_key')
model = llm_config.get('model')

llm = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model=model,
    max_tokens=2000,
    http_client=httpx.Client(verify=False),
    temperature=0.0,
)

