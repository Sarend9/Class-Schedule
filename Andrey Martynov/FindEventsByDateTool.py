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


def merge_date_time(date: str, time: str = None, default_time: str = "00:00") -> str:
    """Возвращает строку вида YYYY-MM-DD HH:MM (или default_time, если time=None/пусто)"""
    if date is None:
        return None
    if time and time.strip():
        return f"{date} {time.strip()}"
    return f"{date} {default_time}"


def next_day(date: str) -> str:
    """Возвращает дату, увеличенную на 1 (строка)"""
    # sqlite примет '+1 day', но тут считаем явно
    import datetime
    d = datetime.datetime.strptime(date, "%Y-%m-%d")
    d += datetime.timedelta(days=1)
    return d.strftime("%Y-%m-%d")


class FindEventsByDate(BaseTool):
    name: str = "FindEventsByDate"
    description: str = (
        "Находит события по дате, периоду, моменту и временному диапазону.\n"
        "Передайте только start_date (YYYY-MM-DD), чтобы найти события за день.\n"
        "Передайте start_date + end_date (YYYY-MM-DD), чтобы найти события за период.\n"
        "Передайте start_date и start_time, чтобы найти события, затрагивающие этот момент времени.\n"
        "Передайте start_date, start_time, end_date, end_time для поиска за период\n"
        "Примеры:\n"
        '{"start_date": "2026-07-01"}\n'
        '{"start_date": "2026-07-11", "end_date": "2026-07-13"}\n'
        '{"start_date": "2026-07-01", "start_time": "10:30"}\n'
        '{"start_date": "2026-07-01", "start_time": "09:00", "end_date": "2026-07-01", "end_time": "13:00"}'
    )

    def _run(self, query_json: str) -> Any:
        try:
            data = json.loads(query_json)
        except json.JSONDecodeError:
            return "Некорректный JSON на входе"

        start_date = data.get("start_date")
        start_time = data.get("start_time")
        end_date = data.get("end_date")
        end_time = data.get("end_time")

        # --- 1. Строим временной интервал запроса ---
        if not start_date:
            return "start_date обязателен"

        if start_time or end_time:  # если есть время, работаем поминутно
            # Если только start_time — ищем момент времени
            period_start = merge_date_time(start_date, start_time, "00:00")
            if end_date or end_time:
                period_end = merge_date_time(end_date or start_date, end_time, "23:59")
            else:
                # Момент: ставим минимальный интервал поисковый, например 1 минута (или совпадение)
                period_end = period_start  # отлично работает для поиска моментов времени
        elif end_date:
            # Даты без времени: ищем все события, затрагивающие данный период включительно
            period_start = merge_date_time(start_date, None, "00:00")
            # период до следующего дня после end_date 00:00, чтобы включительно
            period_end = merge_date_time(next_day(end_date), None, "00:00")
        else:
            # Только дата — ищем все за день (от start_date 00:00 до start_date 23:59:59 включительно)
            period_start = merge_date_time(start_date, None, "00:00")
            period_end = merge_date_time(next_day(start_date), None, "00:00")

        # --- 2. Формируем SQL: пересечение периодов ---
        # Для каждого события определяем:
        #   - event_start = начало события (date + time или date + 00:00)
        #   - event_end   = окончание события (end_date + end_time или если нет, start_date + 23:59, либо start_date + 1 day 00:00)
        # Пересечение: event_start < period_end AND event_end > period_start

        sql = """
            SELECT * FROM events
            WHERE
                -- начало события
                datetime(
                    start_date || ' ' || COALESCE(NULLIF(start_time,''), '00:00')
                ) < :period_end
                AND
                datetime(
                    -- если нет end_date, то берём start_date, если нет end_time — конец дня '23:59'
                    COALESCE(end_date, start_date) || ' ' ||
                    COALESCE(NULLIF(end_time,''), '23:59')
                ) > :period_start
        """
        params = {
            "period_start": period_start,
            "period_end": period_end
        }

        db = sqlite3.connect(db_path)
        db.row_factory = sqlite3.Row
        result = db.execute(sql, params).fetchall()
        db.close()

        if not result:
            return "Событий не найдено"

        # Человекочитаемый вывод
        events_list = []
        for row in result:
            event_str = f'{row["event"]} ({row["start_date"]}'
            if row['start_time']:
                event_str += f' {row["start_time"]}'
            if row['end_date']:
                event_str += f' - {row["end_date"]}'
                if row['end_time']:
                    event_str += f' {row["end_time"]}'
            event_str += ')'
            events_list.append(event_str)
        return "Найдено:\n" + "\n".join(events_list)


find_events_by_date = FindEventsByDate()

if __name__ == "__main__":
    # Проверки на все кейсы из задания:
    print(find_events.run('{"start_date": "2026-07-01"}'))
    print(find_events.run('{"start_date": "2026-07-11", "end_date": "2026-07-13"}'))
    print(find_events.run('{"start_date": "2026-07-01", "start_time": "10:30"}'))
    print(find_events.run(
        '{"start_date": "2026-07-01", "start_time": "09:00", "end_date": "2026-07-01", "end_time": "13:00"}'))
