import mysql.connector as mysql
import os
import dotenv
import csv

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

for i in range(len(data)):
    query = """SELECT s.name, s.second_name, g.title, b.title, s2.title, l.title, m.value
    FROM students s JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m  ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects s2 ON l.subject_id = s2.id
    WHERE s.name = (%s)
    AND s.second_name = (%s)
    AND g.title = (%s)
    AND b.title = (%s)
    AND s2.title = (%s)
    AND l.title = (%s)
    AND m.value = (%s)"""
    values = [data[i]['name'],
              data[i]['second_name'],
              data[i]['group_title'],
              data[i]['book_title'],
              data[i]['subject_title'],
              data[i]['lesson_title'],
              data[i]['mark_value']]
    cursor.execute(query, values)
    result = (cursor.fetchone())
    if result is None:
        print(data[i])

db.close()
