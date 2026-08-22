import mysql.connector as mysql

db = mysql.connect(
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    database="st-onl"
)

cursor = db.cursor(dictionary=True)

# Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
# 1.Создайте студента (student)

query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values = ('Max', 'Payne')
cursor.execute(query, values)
student_table_id = cursor.lastrowid

db.commit()

# 2.Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [('Python Testing', student_table_id),
          ('Java Testing', student_table_id),
          ('JavaScript Testing', student_table_id)]
cursor.executemany(query, values)
books_table_id_3 = cursor.lastrowid
books_table_id_2 = books_table_id_3 - 1
books_table_id_1 = books_table_id_3 - 2

db.commit()

# 3.Создайте группу (group) и определите своего студента туда

query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('MyWorkGroup', 'feb 2026', 'nov 2026')
cursor.execute(query, values)
group_table_id = cursor.lastrowid

query = f"UPDATE students SET group_id = {group_table_id} WHERE id = {student_table_id}"
cursor.execute(query)

db.commit()

# 4.Создайте несколько учебных предметов (subjects)

query = "INSERT INTO subjects (title) VALUES (%s)"
values = [('Math2026',),
          ('History2026',),
          ('Sport2026',)]
cursor.executemany(query, values)
subject_table_id_3 = cursor.lastrowid
subject_table_id_2 = subject_table_id_3 - 1
subject_table_id_1 = subject_table_id_3 - 2

db.commit()

# 5.Создайте по два занятия для каждого предмета (lessons)

query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = [('lesson1', subject_table_id_1),
          ('lesson2', subject_table_id_1),
          ('lesson1', subject_table_id_2),
          ('lesson2', subject_table_id_2),
          ('lesson1', subject_table_id_3),
          ('lesson2', subject_table_id_3)]
cursor.executemany(query, values)
lesson_table_id_6 = cursor.lastrowid
lesson_table_id_5 = lesson_table_id_6 - 1
lesson_table_id_4 = lesson_table_id_6 - 2
lesson_table_id_3 = lesson_table_id_6 - 3
lesson_table_id_2 = lesson_table_id_6 - 4
lesson_table_id_1 = lesson_table_id_6 - 5

db.commit()

# 6.Поставьте своему студенту оценки (marks) для всех созданных вами занятий

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = [('10', lesson_table_id_6, student_table_id),
          ('9', lesson_table_id_5, student_table_id),
          ('8', lesson_table_id_4, student_table_id),
          ('7', lesson_table_id_3, student_table_id),
          ('6', lesson_table_id_2, student_table_id),
          ('5', lesson_table_id_1, student_table_id)]
cursor.executemany(query, values)

db.commit()

# Получите информацию из базы данных:
# 1.Все оценки студента

query = f"SELECT * FROM marks WHERE student_id = {student_table_id}"
cursor.execute(query)
print(cursor.fetchall())

# 2.Все книги, которые находятся у студента

query = f"SELECT * FROM books WHERE taken_by_student_id = {student_table_id}"
cursor.execute(query)
print(cursor.fetchall())

# 3.Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий
# и предметов (всё одним запросом с использованием Join)

query = f"""SELECT * FROM students s JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m  ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects s2 ON l.subject_id = s2.id
WHERE s.id = {student_table_id}"""
cursor.execute(query)
print(cursor.fetchall())

db.close()
