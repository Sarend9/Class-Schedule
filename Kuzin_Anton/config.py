import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_FILENAME = "schedule.db"
DB_PATH = os.path.join(DATA_DIR, DB_FILENAME)

os.makedirs(DATA_DIR, exist_ok=True)
