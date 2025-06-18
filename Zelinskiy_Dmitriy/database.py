import calendar
from datetime import datetime

def generate_schedule_two_same_lessons_per_day_with_break(year, month):
    _, num_days = calendar.monthrange(year, month)

    subjects = [
        "История и философия науки",
        "Иностранный язык",
        "Языки и методы программирования вычислительных систем",
        "Современные средства разработки программ для вычислительных систем"
    ]

    lessons_times = [
        "18:00-19:30 (6 Пара)",
        "19:40-21:10 (7 Пара)"
    ]

    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    schedule = {}
    subject_index = 0

    for day in range(1, num_days + 1):
        date = datetime(year, month, day)
        weekday_index = date.weekday()
        weekday_name = days_of_week[weekday_index]
        key = f"{date.strftime('%Y-%m-%d')} ({weekday_name})"

        if weekday_index >5:  # будние дни
            subject = subjects[subject_index % len(subjects)]
            day_lessons = [
                (lessons_times[0], subject),
                ("19:30-19:40", "Перерыв"),
                (lessons_times[1], subject)
            ]
            schedule[key] = day_lessons
            subject_index += 1
        else:
            schedule[key] = ["Занятий в этот день нет"]

    return schedule

# Пример использования:
year = 2025
month = 6
schedule = generate_schedule_two_same_lessons_per_day_with_break(year, month)

for date_str, lessons in schedule.items():
    print(f"{date_str}:")
    if lessons == ["Занятий в этот день нет"]:
        print(f"  {lessons[0]}")
    else:
        for time, subject in lessons:
            if time == "Перерыв":
                print(f"  {time}")
            else:
                print(f"  {time} - {subject}")
    print()
