from datetime import datetime, timedelta
import calendar

# Список предметов для заполнения расписания
SUBJECTS = [
    "Английский язык",
    "История и философия науки",
    "Современные средства разработки программ для вычислительных систем",
    "Языки и методы программирования вычислительных систем"
]


def generate_full_month_schedule(year: int, month: int):
    days_in_month = calendar.monthrange(year, month)[1]
    schedule = []

    for day in range(1, days_in_month + 1):
        date_obj = datetime(year, month, day)
        date_str = date_obj.strftime("%Y-%m-%d")

        # Выбираем предмет циклично из списка
        subject = SUBJECTS[(day - 1) % len(SUBJECTS)]

        # Для примера время — 10:00 + (день % 4) часов, чтобы немного варьировать
        hour = 10 + ((day - 1) % 4)
        time_str = f"{hour:02d}:00"

        lesson = {
            "date": date_str,
            "time": time_str,
            "description": subject
        }
        schedule.append(lesson)
    return schedule


def print_full_month_schedule(year: int, month: int, schedule: list):
    days_in_month = calendar.monthrange(year, month)[1]
    schedule_sorted = sorted(schedule, key=lambda l: (l["date"], l["time"]))
    print(f"Расписание занятий на {year}-{month:02d}:\n")

    for day in range(1, days_in_month + 1):
        current_date = datetime(year, month, day)
        date_str = current_date.strftime("%Y-%m-%d")
        lessons_today = [lesson for lesson in schedule_sorted if lesson["date"] == date_str]

        print(f"{date_str} ({calendar.day_name[current_date.weekday()]})")
        for lesson in lessons_today:
            print(f"  {lesson['time']} - {lesson['description']}")
        print()


if __name__ == "__main__":
    year = 2025
    month = 6
    schedule = generate_full_month_schedule(year, month)
    print_full_month_schedule(year, month, schedule)
