import calendar
from datetime import datetime, timedelta

# Пример расписания на день (понедельник-пятница)
# Формат: (время начала, время окончания, описание)
schedule_template = [
    ("08:30", "09:15", "Урок 1"),
    ("09:15", "09:25", "Малая перемена"),
    ("09:25", "10:10", "Урок 2"),
    ("10:10", "10:20", "Малая перемена"),
    ("10:20", "11:05", "Урок 3"),
    ("11:05", "11:25", "Большая перемена"),
    ("11:25", "12:10", "Урок 4"),
    ("12:10", "12:20", "Малая перемена"),
    ("12:20", "13:05", "Урок 5"),
]

# Пример предметов для 8А класса на каждый день недели (Пн-Пт)
subjects = {
    0: ["Математика", "Русский язык", "Физика", "История", "Литература"],  # Понедельник
    1: ["Английский язык", "Биология", "Математика", "Физкультура", "Химия"],  # Вторник
    2: ["Информатика", "Русский язык", "География", "Математика", "Обществознание"],  # Среда
    3: ["Физика", "Литература", "Английский язык", "История", "Технология"],  # Четверг
    4: ["Биология", "Математика", "Физкультура", "Химия", "Музыка"],  # Пятница
}

def print_schedule_for_month(year, month):
    cal = calendar.Calendar(firstweekday=0)  # Понедельник=0
    print(f"Расписание занятий 8А класса на {calendar.month_name[month]} {year}\n")

    for day in cal.itermonthdates(year, month):
        if day.month != month:
            continue  # пропускаем дни не из текущего месяца

        weekday = day.weekday()
        # Выходные
        if weekday >= 5:
            print(f"{day.strftime('%d.%m.%Y')} ({calendar.day_name[weekday]}): выходной")
            print()
            continue

        print(f"{day.strftime('%d.%m.%Y')} ({calendar.day_name[weekday]}):")
        daily_subjects = subjects.get(weekday, [])

        for i, (start, end, lesson_type) in enumerate(schedule_template):
            if "Урок" in lesson_type:
                # Определяем номер урока и подставляем предмет
                lesson_num = int(lesson_type.split()[1]) - 1
                subject = daily_subjects[lesson_num] if lesson_num < len(daily_subjects) else "Свободное время"
                print(f"  {start} - {end}: {subject}")
            else:
                # Перемена
                print(f"  {start} - {end}: {lesson_type}")

        print()  # пустая строка после каждого дня

# Пример вызова для мая 2025
print_schedule_for_month(2025, 5)
