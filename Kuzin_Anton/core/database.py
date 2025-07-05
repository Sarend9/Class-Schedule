import sqlite3
from sqlite3 import Connection, Cursor
from typing import Optional

import config

SCHEMA_SQL = """
-- Таблица предметов
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Можно хранить группы (например, «ИС-01», «ПИ-02» и т. д.)
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Преподаватели (опционально)
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Аудитории (опционально)
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Таблица расписания: привязка предмет + группа + время + аудитория + преподаватель + ДАТА
CREATE TABLE IF NOT EXISTS schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    group_id INTEGER NOT NULL,
    teacher_id INTEGER,
    room_id INTEGER,
    schedule_date TEXT NOT NULL,        -- НОВОЕ ПОЛЕ: Хранить в формате YYYY-MM-DD
    start_time TEXT NOT NULL,           -- хранить в формате "HH:MM"
    end_time TEXT NOT NULL,             -- хранить в формате "HH:MM"
    FOREIGN KEY (subject_id) REFERENCES subjects (id) ON DELETE CASCADE,
    FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE SET NULL,
    FOREIGN KEY (room_id) REFERENCES rooms (id) ON DELETE SET NULL
);
"""


class Database:

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or config.DB_PATH
        self.conn: Connection = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._initialize_schema()

    def _initialize_schema(self) -> None:
        cursor = self.conn.cursor()
        cursor.executescript(SCHEMA_SQL)
        self.conn.commit()

    def execute(self, sql: str, params: tuple = ()) -> Cursor:
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        self.conn.commit()
        return cursor

    def fetchall(self, sql: str, params: tuple = ()) -> list:
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        return cursor.fetchall()

    def fetchone(self, sql: str, params: tuple = ()):
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        return cursor.fetchone()

    def close(self):
        if self.conn:
            self.conn.close()
        Database._instance = None
