import sqlite3
from datetime import datetime

conn = sqlite3.connect("data/attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    name TEXT,
    time TEXT
)
""")
conn.commit()

def save_attendance(name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO attendance VALUES (?, ?)", (name, now))
    conn.commit()
    print(f"Đã chấm công: {name} - {now}")