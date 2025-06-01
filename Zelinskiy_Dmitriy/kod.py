import datetime
import json
import os
from typing import List, Dict, Optional

DATA_FILE = "schedule_data.json"

SUBJECTS = [
    "Английский язык",
    "История и философия науки",
    "Современные средства разработки программ для вычислительных систем",
    "Языки и методы программирования вычислительных систем"
]

COMMANDS = {
    "help": "Показать список доступных команд",
    "add": "Добавить новое занятие",
    "view": "Просмотреть расписание (день, неделя, месяц)",
    "edit": "Редактировать занятие",
    "delete": "Удалить занятие",
    "exit": "Выйти из программы"
}

def load_schedule() -> Dict[str, List[Dict]]:
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            print("Ошибка при загрузке данных. Начинаем с пустого расписания.")
    return {}

def save_schedule(schedule: Dict[str, List[Dict]]):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(schedule, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def print_welcome():
    print("="*50)
    print("Календарь занятий (консольное приложение)")
    print("Позволяет добавлять, просматривать, редактировать и удалять занятия.")
    print("Форматы даты: ГГГГ-ММ-ДД, время: чч:мм (24-часовой формат).")
    print("Введите 'help' для списка команд.")
    print("="*50)

def print_help():
    print("\nДоступные команды:")
    for cmd, desc in COMMANDS.items():
        print(f"  {cmd} - {desc}")
    print()

def input_date(prompt: str) -> Optional[str]:
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Ошибка: дата должна быть в формате ГГГГ-ММ-ДД. Попробуйте снова или введите пустую строку для отмены.")
            if date_str == "":
                return None

def input_time(prompt: str) -> Optional[str]:
    while True:
        time_str = input(prompt).strip()
        try:
            datetime.datetime.strptime(time_str, "%H:%M")
            return time_str
        except ValueError:
            print("Ошибка: время должно быть в формате чч:мм (24-часовой формат). Попробуйте снова или введите пустую строку для отмены.")
            if time_str == "":
                return None

def choose_subject() -> Optional[str]:
    print("Выберите предмет из списка:")
    for i, subj in enumerate(SUBJECTS, 1):
        print(f"  {i}. {subj}")
    while True:
        choice = input("Введите номер предмета или введите название вручную (пустая строка для отмены): ").strip()
        if choice == "":
            return None
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(SUBJECTS):
                return SUBJECTS[idx - 1]
            else:
                print("Неверный номер. Попробуйте снова.")
        else:
            # Можно ввести название вручную
            return choice

def add_lesson(schedule: Dict[str, List[Dict]]):
    print("\nДобавление нового занятия. Для отмены введите пустую строку на любом шаге.")
    date = input_date("Введите дату занятия (ГГГГ-ММ-ДД): ")
    if date is None:
        print("Добавление занятия отменено.")
        return
    time = input_time("Введите время занятия (чч:мм): ")
    if time is None:
        print("Добавление занятия отменено.")
        return
    subject = choose_subject()
    if subject is None:
        print("Добавление занятия отменено.")
        return

    lesson = {
        "time": time,
        "subject": subject
    }
    if date not in schedule:
        schedule[date] = []
    # Проверка на конфликт времени
    for l in schedule[date]:
        if l["time"] == time:
            print(f"Ошибка: на {date} в {time} уже есть занятие '{l['subject']}'.")
            return
    schedule[date].append(lesson)
    schedule[date].sort(key=lambda x: x["time"])
    save_schedule(schedule)
    print("Занятие успешно добавлено.")

def print_lessons(lessons: List[Dict]):
    if not lessons:
        print("Занятий нет.")
        return
    for idx, lesson in enumerate(lessons, 1):
        print(f"{idx}. {lesson['time']} - {lesson['subject']}")

def view_schedule(schedule: Dict[str, List[Dict]]):
    print("\nПросмотр расписания.")
    print("Выберите период просмотра:")
    print("  1. День")
    print("  2. Неделя")
    print("  3. Месяц")
    choice = input("Введите номер (1-3) или пустую строку для отмены: ").strip()
    if choice == "":
        print("Просмотр отменён.")
        return
    today = datetime.date.today()

    if choice == "1":
        date = input_date("Введите дату (ГГГГ-ММ-ДД): ")
        if date is None:
            print("Просмотр отменён.")
            return
        lessons = schedule.get(date, [])
        print(f"\nРасписание на {date}:")
        print_lessons(lessons)

    elif choice == "2":
        date = input_date("Введите дату, входящую в неделю (ГГГГ-ММ-ДД): ")
        if date is None:
            print("Просмотр отменён.")
            return
        dt = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        start_week = dt - datetime.timedelta(days=dt.weekday())  # Понедельник
        print(f"\nРасписание на неделю с {start_week} по {start_week + datetime.timedelta(days=6)}:")
        any_lessons = False
        for i in range(7):
            day = start_week + datetime.timedelta(days=i)
            day_str = day.isoformat()
            lessons = schedule.get(day_str, [])
            if lessons:
                any_lessons = True
                print(f"\n{day_str}:")
                print_lessons(lessons)
        if not any_lessons:
            print("Занятий на эту неделю нет.")

    elif choice == "3":
        date = input_date("Введите дату, входящую в месяц (ГГГГ-ММ-ДД): ")
        if date is None:
            print("Просмотр отменён.")
            return
        dt = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        year = dt.year
        month = dt.month
        print(f"\nРасписание на {year}-{month:02d}:")
        any_lessons = False
        for day_str in sorted(schedule.keys()):
            day_dt = datetime.datetime.strptime(day_str, "%Y-%m-%d").date()
            if day_dt.year == year and day_dt.month == month:
                lessons = schedule[day_str]
                any_lessons = True
                print(f"\n{day_str}:")
                print_lessons(lessons)
        if not any_lessons:
            print("Занятий на этот месяц нет.")
    else:
        print("Некорректный выбор.")

def select_lesson(schedule: Dict[str, List[Dict]], prompt: str) -> Optional[tuple]:
    """
    Позволяет выбрать занятие по дате и времени из расписания.
    Возвращает (date, lesson_index) или None.
    """
    date = input_date("Введите дату занятия (ГГГГ-ММ-ДД) или пустую строку для отмены: ")
    if date is None:
        return None
    lessons = schedule.get(date, [])
    if not lessons:
        print(f"На дату {date} занятий нет.")
        return None
    print(f"Занятия на {date}:")
    print_lessons(lessons)
    while True:
        choice = input(prompt).strip()
        if choice == "":
            return None
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(lessons):
                return (date, idx - 1)
            else:
                print("Неверный номер занятия. Попробуйте снова.")
        else:
            print("Введите номер занятия.")

def edit_lesson(schedule: Dict[str, List[Dict]]):
    print("\nРедактирование занятия.")
    sel = select_lesson(schedule, "Введите номер занятия для редактирования (или пустую строку для отмены): ")
    if sel is None:
        print("Редактирование отменено.")
        return
    date, idx = sel
    lesson = schedule[date][idx]
    print(f"Текущее занятие: {lesson['time']} - {lesson['subject']}")
    print("Введите новые данные или оставьте пустым для сохранения текущего значения.")
    new_date = input_date(f"Новая дата (текущая {date}): ")
    if new_date is None:
        new_date = date
    new_time = input_time(f"Новое время (текущее {lesson['time']}): ")
    if new_time is None:
        new_time = lesson["time"]
    print("Выберите новый предмет:")
    new_subject = choose_subject()
    if new_subject is None:
        new_subject = lesson["subject"]

    # Проверка конфликта по времени на новой дате
    if new_date != date or new_time != lesson["time"]:
        lessons_on_new_date = schedule.get(new_date, [])
        for i, l in enumerate(lessons_on_new_date):
            if l["time"] == new_time and not (new_date == date and i == idx):
                print(f"Ошибка: на {new_date} в {new_time} уже есть занятие '{l['subject']}'. Редактирование отменено.")
                return

    # Удаляем старую запись
    schedule[date].pop(idx)
    if not schedule[date]:
        del schedule[date]

    # Добавляем новую запись
    if new_date not in schedule:
        schedule[new_date] = []
    schedule[new_date].append({
        "time": new_time,
        "subject": new_subject
    })
    schedule[new_date].sort(key=lambda x: x["time"])
    save_schedule(schedule)
    print("Занятие успешно отредактировано.")

def delete_lesson(schedule: Dict[str, List[Dict]]):
    print("\nУдаление занятия.")
    sel = select_lesson(schedule, "Введите номер занятия для удаления (или пустую строку для отмены): ")
    if sel is None:
        print("Удаление отменено.")
        return
    date, idx = sel
    lesson = schedule[date][idx]
    confirm = input(f"Вы уверены, что хотите удалить занятие {lesson['time']} - {lesson['subject']}? (д/н): ").strip().lower()
    if confirm == "д":
        schedule[date].pop(idx)
        if not schedule[date]:
            del schedule[date]
        save_schedule(schedule)
        print("Занятие удалено.")
    else:
        print("Удаление отменено.")

def main():
    schedule = load_schedule()
    print_welcome()

    while True:
        cmd = input("\nВведите команду ('help' для справки): ").strip().lower()
        if cmd == "help":
            print_help()
        elif cmd == "add":
            add_lesson(schedule)
        elif cmd == "view":
            view_schedule(schedule)
        elif cmd == "edit":
            edit_lesson(schedule)
        elif cmd == "delete":
            delete_lesson(schedule)
        elif cmd == "exit":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неизвестная команда. Введите 'help' для списка команд.")

if __name__ == "__main__":
    main()
