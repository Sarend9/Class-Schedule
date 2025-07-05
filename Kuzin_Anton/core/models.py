import sqlite3
from typing import List, Dict, Optional

from .database import Database


class ScheduleManager:
    def __init__(self):
        self._db = Database()

    def add_subject(self, name: str) -> Optional[int]:
        try:
            cursor = self._db.execute("INSERT INTO subjects (name) VALUES (?)", (name.strip(),))
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            row = self._db.fetchone("SELECT id FROM subjects WHERE name = ?", (name.strip(),))
            return row["id"] if row else None

    def get_all_subjects(self) -> List[Dict]:
        rows = self._db.fetchall("SELECT id, name FROM subjects ORDER BY name")
        return [dict(r) for r in rows]

    def add_group(self, name: str) -> Optional[int]:
        try:
            cursor = self._db.execute("INSERT INTO groups (name) VALUES (?)", (name.strip(),))
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            row = self._db.fetchone("SELECT id FROM groups WHERE name = ?", (name.strip(),))
            return row["id"] if row else None

    def get_all_groups(self) -> List[Dict]:
        rows = self._db.fetchall("SELECT id, name FROM groups ORDER BY name")
        return [dict(r) for r in rows]

    def add_teacher(self, name: str) -> Optional[int]:
        try:
            cur = self._db.execute("INSERT INTO teachers (name) VALUES (?)", (name.strip(),))
            return cur.lastrowid
        except sqlite3.IntegrityError:
            row = self._db.fetchone("SELECT id FROM teachers WHERE name = ?", (name.strip(),))
            return row["id"] if row else None

    def get_all_teachers(self) -> List[Dict]:
        rows = self._db.fetchall("SELECT id, name FROM teachers ORDER BY name")
        return [dict(r) for r in rows]

    def add_room(self, name: str) -> Optional[int]:
        try:
            cur = self._db.execute("INSERT INTO rooms (name) VALUES (?)", (name.strip(),))
            return cur.lastrowid
        except sqlite3.IntegrityError:
            row = self._db.fetchone("SELECT id FROM rooms WHERE name = ?", (name.strip(),))
            return row["id"] if row else None

    def get_all_rooms(self) -> List[Dict]:
        rows = self._db.fetchall("SELECT id, name FROM rooms ORDER BY name")
        return [dict(r) for r in rows]

    def add_schedule_entry(
            self,
            subject_id: int,
            group_id: int,
            schedule_date: str,
            start_time: str,
            end_time: str,
            teacher_id: Optional[int] = None,
            room_id: Optional[int] = None
    ) -> Optional[int]:
        cursor = self._db.execute(
            """INSERT INTO schedule (subject_id, group_id, teacher_id, room_id, schedule_date, start_time, end_time)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (subject_id, group_id, teacher_id, room_id, schedule_date, start_time, end_time)
        )
        return cursor.lastrowid

    def get_full_schedule(self) -> List[Dict]:
        """
        Возвращает все расписание для всех групп, упорядоченное по дате и времени.
        """
        rows = self._db.fetchall(
            """SELECT s.id, subjects.name AS subject, groups.name AS group_name,
                      teachers.name AS teacher, rooms.name AS room,
                      s.schedule_date, s.start_time, s.end_time
               FROM schedule s
               JOIN subjects ON subjects.id = s.subject_id
               JOIN groups ON groups.id = s.group_id
               LEFT JOIN teachers ON teachers.id = s.teacher_id
               LEFT JOIN rooms ON rooms.id = s.room_id
               ORDER BY s.schedule_date, s.start_time, groups.name"""
        )
        return [dict(r) for r in rows]

    def get_filtered_schedule(self, search_query: Optional[str] = None) -> List[Dict]:
        """
        Возвращает расписание, отфильтрованное по поисковому запросу.
        Поиск выполняется по предмету, группе, преподавателю или аудитории.
        """
        sql = """SELECT s.id, subjects.name AS subject, groups.name AS group_name,
                        teachers.name AS teacher, rooms.name AS room,
                        s.schedule_date, s.start_time, s.end_time
                 FROM schedule s
                 JOIN subjects ON subjects.id = s.subject_id
                 JOIN groups ON groups.id = s.group_id
                 LEFT JOIN teachers ON teachers.id = s.teacher_id
                 LEFT JOIN rooms ON rooms.id = s.room_id"""
        params = []

        if search_query:
            search_term = f"%{search_query}%"
            sql += """ WHERE subjects.name LIKE ? OR groups.name LIKE ?
                       OR teachers.name LIKE ? OR rooms.name LIKE ?"""
            params.extend([search_term, search_term, search_term, search_term])

        sql += " ORDER BY s.schedule_date, s.start_time, groups.name"

        rows = self._db.fetchall(sql, tuple(params))
        return [dict(r) for r in rows]

    def get_schedule_for_date(self, date_str: str) -> List[Dict]:
        """
        Возвращает все записи расписания для заданной даты (YYYY-MM-DD),
        упорядоченные по времени и группе.
        """
        rows = self._db.fetchall(
            """SELECT s.id, subjects.name AS subject, groups.name AS group_name,
                      teachers.name AS teacher, rooms.name AS room,
                      s.schedule_date, s.start_time, s.end_time
               FROM schedule s
               JOIN subjects ON subjects.id = s.subject_id
               JOIN groups ON groups.id = s.group_id
               LEFT JOIN teachers ON teachers.id = s.teacher_id
               LEFT JOIN rooms ON rooms.id = s.room_id
               WHERE s.schedule_date = ?
               ORDER BY s.start_time, groups.name""",
            (date_str,)
        )
        return [dict(r) for r in rows]

    def delete_schedule_entry(self, entry_id: int) -> bool:
        cursor = self._db.execute("DELETE FROM schedule WHERE id = ?", (entry_id,))
        return cursor.rowcount > 0

    def get_distinct_schedule_dates(self) -> List[str]:
        rows = self._db.fetchall("SELECT DISTINCT schedule_date FROM schedule ORDER BY schedule_date")
        return [row["schedule_date"] for row in rows]
