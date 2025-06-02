import random
from typing import Optional

from PySide6.QtCore import QDate, Qt, QTime
from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView, QAbstractItemView

from core.models import ScheduleManager
from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.schedule_manager = ScheduleManager()

        self._initialize_database_and_data()

        self.ui.calendarWidget.selectionChanged.connect(self.display_schedule_for_selected_date)
        self.ui.addEntryButton.clicked.connect(self.add_new_schedule_entry)
        self.ui.deleteDailyEntryButton.clicked.connect(self.delete_selected_schedule_entry)
        self.ui.deleteAllEntryButton.clicked.connect(self.delete_selected_schedule_entry_from_all)

        self.ui.allScheduleTable.itemClicked.connect(self.jump_to_event_date)

        self.ui.applyFilterButton.clicked.connect(self.apply_schedule_filter)
        self.ui.clearFilterButton.clicked.connect(self.clear_schedule_filter)
        self.ui.searchLineEdit.returnPressed.connect(self.apply_schedule_filter)

        self._configure_tables()
        self._populate_comboboxes()
        self._highlight_days_with_events()
        self.load_all_schedule()

        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.startTimeEdit.setTime(QTime(9, 0))
        self.ui.endTimeEdit.setTime(QTime(10, 30))

        self.display_schedule_for_selected_date()


    def _initialize_database_and_data(self):
        """Инициализирует БД и добавляет тестовые данные, если БД пуста."""

        subjects = self.schedule_manager.get_all_subjects()
        if not subjects:
            QMessageBox.information(self, "Инициализация", "База данных пуста. Добавляем тестовые данные...")

            # Данные для генерации
            subject_names = [
                "Современные средства разработки программ для вычислительных систем",
                "Языки и методы программирования вычислительных систем",
                "История и философия наук",
                "Английский язык",
                "Математический анализ",
                "Физика",
                "Базы данных",
                "Операционные системы"
            ]
            group_names = ["ИС-01", "ПИ-02", "АСУ-03", "ЭВМ-04"]
            teacher_names = ["Иванов И.И.", "Петрова Е.С.", "Сидоров В.А.", "Козлова Н.М.", "Смирнов Д.П."]
            room_names = ["301", "405", "210", "101", "503", "Л-17"]

            # Добавляем предметы, группы, преподавателей, аудитории и сохраняем их ID
            subject_ids = {name: self.schedule_manager.add_subject(name) for name in subject_names}
            group_ids = {name: self.schedule_manager.add_group(name) for name in group_names}
            teacher_ids = {name: self.schedule_manager.add_teacher(name) for name in teacher_names}
            room_ids = {name: self.schedule_manager.add_room(name) for name in room_names}

            # Генерируем случайные записи расписания
            num_entries = 30  # Количество случайных записей
            current_date = QDate.currentDate()

            for _ in range(num_entries):
                # Случайный предмет
                random_subject_name = random.choice(subject_names)
                subject_id = subject_ids[random_subject_name]

                # Случайная группа
                random_group_name = random.choice(group_names)
                group_id = group_ids[random_group_name]

                # Случайный преподаватель
                random_teacher_name = random.choice(teacher_names)
                teacher_id = teacher_ids.get(random_teacher_name)

                # Случайная аудитория (может быть None)
                random_room_name = random.choice(room_names + [None])
                room_id = room_ids.get(random_room_name) if random_room_name else None

                # Случайная дата в пределах следующих 10 дней
                date_offset = random.randint(0, 9)
                schedule_date = current_date.addDays(date_offset).toString(Qt.ISODate)

                # Случайное время начала и конца
                start_hour = random.randint(8, 17)  # С 8:00 до 17:00
                start_minute = random.choice([0, 30])
                start_time_qtime = QTime(start_hour, start_minute)

                # Продолжительность занятия (например, 1.5 часа)
                end_time_qtime = start_time_qtime.addSecs(int(1.5 * 3600))  # 1.5 часа

                start_time_str = start_time_qtime.toString("HH:mm")
                end_time_str = end_time_qtime.toString("HH:mm")

                self.schedule_manager.add_schedule_entry(
                    subject_id=subject_id,
                    group_id=group_id,
                    schedule_date=schedule_date,
                    start_time=start_time_str,
                    end_time=end_time_str,
                    teacher_id=teacher_id,
                    room_id=room_id
                )

            QMessageBox.information(self, "Инициализация",
                                    f"{num_entries} случайных тестовых записей успешно добавлены.")

        # Обязательно загружаем данные после инициализации/добавления тестовых данных
        self.load_all_schedule()
        self.display_schedule_for_selected_date()

    def _configure_tables(self):
        """Настраивает QTableWidget для отображения расписания на выбранную дату и всех событий."""

        self.ui.dailyScheduleTable.setColumnCount(7)
        self.ui.dailyScheduleTable.setHorizontalHeaderLabels([
            "ID", "Предмет", "Группа", "Начало", "Окончание", "Преподаватель", "Аудитория"
        ])
        self.ui.dailyScheduleTable.setColumnHidden(0, True)
        self.ui.dailyScheduleTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.dailyScheduleTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.dailyScheduleTable.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.allScheduleTable.setColumnCount(8)
        self.ui.allScheduleTable.setHorizontalHeaderLabels([
            "ID", "Дата", "Предмет", "Группа", "Начало", "Окончание", "Преподаватель", "Аудитория"
        ])
        self.ui.allScheduleTable.setColumnHidden(0, True)
        self.ui.allScheduleTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.allScheduleTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.allScheduleTable.setSelectionMode(QAbstractItemView.SingleSelection)

    def _populate_comboboxes(self):
        """Заполняет QComboBox'ы данными из БД."""
        self.ui.subjectComboBox.clear()
        self.ui.groupComboBox.clear()
        self.ui.teacherComboBox.clear()
        self.ui.roomComboBox.clear()

        subjects = self.schedule_manager.get_all_subjects()
        for subject in subjects:
            self.ui.subjectComboBox.addItem(subject["name"], subject["id"])

        groups = self.schedule_manager.get_all_groups()
        for group in groups:
            self.ui.groupComboBox.addItem(group["name"], group["id"])

        teachers = self.schedule_manager.get_all_teachers()
        self.ui.teacherComboBox.addItem("Не выбрано", None)
        for teacher in teachers:
            self.ui.teacherComboBox.addItem(teacher["name"], teacher["id"])

        rooms = self.schedule_manager.get_all_rooms()
        self.ui.roomComboBox.addItem("Не выбрано", None)
        for room in rooms:
            self.ui.roomComboBox.addItem(room["name"], room["id"])

    def display_schedule_for_selected_date(self):
        """Отображает расписание для выбранной в QCalendarWidget даты."""
        selected_date: QDate = self.ui.calendarWidget.selectedDate()
        date_str = selected_date.toString(Qt.ISODate)

        self.ui.selectedDateSchedule.setTitle(f"Расписание на {selected_date.toString('dd.MM.yyyy')}:")

        data = self.schedule_manager.get_schedule_for_date(date_str)
        self.ui.dailyScheduleTable.setRowCount(len(data))

        for row_idx, entry in enumerate(data):
            self.ui.dailyScheduleTable.setItem(row_idx, 0, QTableWidgetItem(str(entry["id"])))
            self.ui.dailyScheduleTable.setItem(row_idx, 1, QTableWidgetItem(entry["subject"]))
            self.ui.dailyScheduleTable.setItem(row_idx, 2, QTableWidgetItem(entry["group_name"]))
            self.ui.dailyScheduleTable.setItem(row_idx, 3, QTableWidgetItem(entry["start_time"]))
            self.ui.dailyScheduleTable.setItem(row_idx, 4, QTableWidgetItem(entry["end_time"]))
            self.ui.dailyScheduleTable.setItem(row_idx, 5, QTableWidgetItem(entry["teacher"] if entry["teacher"] else "Не указан"))
            self.ui.dailyScheduleTable.setItem(row_idx, 6, QTableWidgetItem(entry["room"] if entry["room"] else "Не указана"))

    def load_all_schedule(self, search_query: Optional[str] = None):
        """Загружает и отображает все записи расписания в таблице 'Все события', с возможностью фильтрации."""
        data = self.schedule_manager.get_filtered_schedule(search_query)
        self.ui.allScheduleTable.setRowCount(len(data))

        for row_idx, entry in enumerate(data):
            date_display = QDate.fromString(entry["schedule_date"], Qt.ISODate).toString('dd.MM.yyyy')
            self.ui.allScheduleTable.setItem(row_idx, 0, QTableWidgetItem(str(entry["id"])))
            self.ui.allScheduleTable.setItem(row_idx, 1, QTableWidgetItem(date_display))
            self.ui.allScheduleTable.setItem(row_idx, 2, QTableWidgetItem(entry["subject"]))
            self.ui.allScheduleTable.setItem(row_idx, 3, QTableWidgetItem(entry["group_name"]))
            self.ui.allScheduleTable.setItem(row_idx, 4, QTableWidgetItem(entry["start_time"]))
            self.ui.allScheduleTable.setItem(row_idx, 5, QTableWidgetItem(entry["end_time"]))
            self.ui.allScheduleTable.setItem(row_idx, 6, QTableWidgetItem(entry["teacher"] if entry["teacher"] else "Не указан"))
            self.ui.allScheduleTable.setItem(row_idx, 7, QTableWidgetItem(entry["room"] if entry["room"] else "Не указана"))

    def apply_schedule_filter(self):
        """Применяет фильтр к таблице всех событий."""
        search_text = self.ui.searchLineEdit.text().strip()
        self.load_all_schedule(search_text if search_text else None)

    def clear_schedule_filter(self):
        """Очищает поле поиска и сбрасывает фильтр."""
        self.ui.searchLineEdit.clear()
        self.load_all_schedule()

    def jump_to_event_date(self, item: QTableWidgetItem):
        """Переключает календарь на дату выбранного события."""
        row_index = item.row()
        date_item = self.ui.allScheduleTable.item(row_index, 1)
        if date_item:
            date_str = date_item.text()
            date = QDate.fromString(date_str, 'dd.MM.yyyy')
            self.ui.calendarWidget.setSelectedDate(date)
            self.display_schedule_for_selected_date()

    def add_new_schedule_entry(self):
        """Добавляет новую запись в расписание из полей ввода UI."""
        subject_id = self.ui.subjectComboBox.currentData()
        group_id = self.ui.groupComboBox.currentData()
        schedule_date: QDate = self.ui.dateEdit.date()
        date_str = schedule_date.toString(Qt.ISODate)

        start_time_qtime: QTime = self.ui.startTimeEdit.time()
        end_time_qtime: QTime = self.ui.endTimeEdit.time()

        start_time_str = start_time_qtime.toString("HH:mm")
        end_time_str = end_time_qtime.toString("HH:mm")

        teacher_id = self.ui.teacherComboBox.currentData()
        room_id = self.ui.roomComboBox.currentData()

        if not all([subject_id, group_id, date_str]):
            QMessageBox.warning(self, "Ошибка ввода",
                                "Пожалуйста, заполните все обязательные поля (Предмет, Группа, Дата).")
            return

        if start_time_qtime >= end_time_qtime:
            QMessageBox.warning(self, "Ошибка ввода", "Время начала должно быть раньше времени окончания.")
            return

        try:
            self.schedule_manager.add_schedule_entry(
                subject_id=subject_id,
                group_id=group_id,
                schedule_date=date_str,
                start_time=start_time_str,
                end_time=end_time_str,
                teacher_id=teacher_id,
                room_id=room_id
            )
            QMessageBox.information(self, "Успех", "Запись расписания успешно добавлена.")
            self.display_schedule_for_selected_date()
            self.load_all_schedule()
            self._highlight_days_with_events()
            self._clear_input_fields()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при добавлении записи: {e}")

    def delete_selected_schedule_entry(self):
        """Удаляет выбранную запись из таблицы расписания на выбранную дату."""
        selected_rows = self.ui.dailyScheduleTable.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Удаление", "Пожалуйста, выберите запись для удаления.")
            return

        reply = QMessageBox.question(self, "Подтверждение удаления",
                                     "Вы уверены, что хотите удалить выбранную запись?",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                row_index = selected_rows[0].row()
                schedule_id_item = self.ui.dailyScheduleTable.item(row_index, 0)
                if schedule_id_item:
                    schedule_id = int(schedule_id_item.text())
                    if self.schedule_manager.delete_schedule_entry(schedule_id):
                        QMessageBox.information(self, "Успех", "Запись расписания успешно удалена.")
                        self.display_schedule_for_selected_date()
                        self.load_all_schedule()
                        self._highlight_days_with_events()
                    else:
                        QMessageBox.warning(self, "Ошибка", "Не удалось удалить запись. Возможно, она не найдена.")
                else:
                    QMessageBox.critical(self, "Ошибка", "Не удалось получить ID выбранной записи.")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при удалении записи: {e}")

    def delete_selected_schedule_entry_from_all(self):
        """Удаляет выбранную запись из таблицы 'Все события'."""
        selected_rows = self.ui.allScheduleTable.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Удаление", "Пожалуйста, выберите запись для удаления.")
            return

        reply = QMessageBox.question(self, "Подтверждение удаления",
                                     "Вы уверены, что хотите удалить выбранную запись?",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                row_index = selected_rows[0].row()
                schedule_id_item = self.ui.allScheduleTable.item(row_index, 0)
                if schedule_id_item:
                    schedule_id = int(schedule_id_item.text())
                    if self.schedule_manager.delete_schedule_entry(schedule_id):
                        QMessageBox.information(self, "Успех", "Запись расписания успешно удалена.")
                        self.display_schedule_for_selected_date()
                        self.load_all_schedule()
                        self._highlight_days_with_events()
                    else:
                        QMessageBox.warning(self, "Ошибка", "Не удалось удалить запись. Возможно, она не найдена.")
                else:
                    QMessageBox.critical(self, "Ошибка", "Не удалось получить ID выбранной записи.")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при удалении записи: {e}")

    def _clear_input_fields(self):
        """Очищает поля ввода после добавления."""
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.startTimeEdit.setTime(QTime(9, 0))
        self.ui.endTimeEdit.setTime(QTime(10, 30))

    def _highlight_days_with_events(self):
        """Выделяет в календаре дни, в которые есть события."""
        default_format = QTextCharFormat()
        all_distinct_dates_in_db = self.schedule_manager.get_distinct_schedule_dates()
        for date_str in all_distinct_dates_in_db:
            date = QDate.fromString(date_str, Qt.ISODate)
            self.ui.calendarWidget.setDateTextFormat(date, default_format)

        dates_with_events = self.schedule_manager.get_distinct_schedule_dates()

        format = QTextCharFormat()
        format.setBackground(QColor("lightblue"))

        for date_str in dates_with_events:
            date = QDate.fromString(date_str, Qt.ISODate)
            self.ui.calendarWidget.setDateTextFormat(date, format)
