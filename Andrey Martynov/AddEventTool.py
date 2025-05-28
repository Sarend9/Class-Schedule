import json
from langchain.tools import BaseTool
from typing import Any
import os
import configparser
import sqlite3

# Получаем настройки подключения к БД
config = configparser.ConfigParser()
config.read('config.ini')
db_config = config['database']
db_path = db_config.get('db_path')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_path)
# Создаём подключение к БД
DB = sqlite3.connect(db_path)
DB.execute('''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event TEXT NOT NULL,
    start_date TEXT NOT NULL,
    start_time TEXT,
    end_date TEXT,
    end_time TEXT)
''')
DB.commit()
DB.close()

class AddEvent(BaseTool):
    name: str = "AddEvent"
    description: str = (
        "Сохраняет запланированное событие.\n"
        "Обязательные поля: event (строка), start_date (YYYY-MM-DD).\n"
        "Опциональные поля: start_time (HH:MM), end_date (YYYY-MM-DD), end_time (HH:MM).\n"
        "Если время не указано — событие рассматривается как целый день.\n"
        "Если окончание не указано — оно будет пустым.\n"
        "Пример входа: "
        '{"event": "Совещание", "start_date": "2026-07-01", "start_time": "10:00", "end_date": "2026-07-01", "end_time":"11:00"}\n'
        '{"event": "День рождения", "start_date": "2027-03-10"}\n'
        '{"event": "Отпуск", "start_date": "2025-07-11", "end_date": "2025-07-13"}'
    )

    def _run(self, event_json: str) -> Any:
        try:
            data = json.loads(event_json)
        except json.JSONDecodeError:
            return "Некорректный JSON на входе"

        event = data.get("event")
        start_date = data.get("start_date")
        start_time = data.get("start_time")
        end_date = data.get("end_date")
        end_time = data.get("end_time")

        # Проверяем обязательные поля
        if not event or not start_date:
            return "Не заполнены обязательные поля: event и start_date"

        try:
            # Создаём подключение к БД
            DB = sqlite3.connect(db_path)
            cursor = DB.cursor()
            cursor.execute(
                "INSERT INTO events (event, start_date, start_time, end_date, end_time) VALUES (?, ?, ?, ?, ?)",
                (event, start_date, start_time, end_date, end_time)
            )
            DB.commit()
            event_id = cursor.lastrowid
            DB.close()
            return f'Событие "{event}" добавлено в календарь'
        except Exception as e:
            return f"Ошибка при работе с БД: {str(e)}"

add_event = AddEvent()

if __name__ == "__main__":
    print(add_event.run('{"event": "Конференция", "start_date": "2026-07-01", "start_time": "10:30"}'))
    print(add_event.run('{"event": "Праздник", "start_date": "2026-07-11", "end_date": "2026-07-13"}'))
    print(add_event.run('{"event": "День рождения", "start_date": "2026-07-10"}'))