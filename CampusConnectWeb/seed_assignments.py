import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

BASE_DIRECTORY = Path(__file__).resolve().parent
load_dotenv(BASE_DIRECTORY / ".env", override=True)

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    use_pure=True,
)

cursor = connection.cursor(dictionary=True)

sample_assignments = [
    (
        "COSC 369",
        "Final Project Presentation",
        "Present the completed CampusConnect Flask and MySQL application.",
        "2026-11-13 19:00:00",
    ),
    (
        "COSC 208",
        "Programming Assignment",
        "Complete the assigned programming exercise and submit the source code.",
        "2026-11-16 23:59:00",
    ),
]

for course_code, title, description, due_date in sample_assignments:
    cursor.execute(
        "SELECT course_id FROM courses WHERE course_code = %s LIMIT 1",
        (course_code,),
    )
    course = cursor.fetchone()

    if not course:
        print(f"Course not found: {course_code}")
        continue

    cursor.execute(
        """
        SELECT assignment_id
        FROM assignments
        WHERE course_id = %s AND title = %s
        LIMIT 1
        """,
        (course["course_id"], title),
    )

    if cursor.fetchone():
        print(f"Already exists: {course_code} - {title}")
        continue

    cursor.execute(
        """
        INSERT INTO assignments
            (course_id, title, description, due_date)
        VALUES
            (%s, %s, %s, %s)
        """,
        (course["course_id"], title, description, due_date),
    )
    print(f"Added: {course_code} - {title}")

connection.commit()
cursor.close()
connection.close()

print("Sample assignments are ready.")
