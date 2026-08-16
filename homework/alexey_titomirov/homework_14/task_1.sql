-- Создайте в базе данных полный набор информации о студенте, заполнив все таблички:

-- 1.Создайте студента (student)

INSERT INTO students (name, second_name) VALUES ('Max', 'Payne');

-- 2.Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

INSERT INTO books (title, taken_by_student_id)
VALUES ('Python Testing', 23073), ('Java Testing', 23073), ('JavaScript Testing', 23073);

-- 3.Создайте группу (group) и определите своего студента туда

INSERT INTO `groups` (title, start_date, end_date) VALUES ('MyWorkGroup', 'feb 2026', 'nov 2026');

UPDATE students SET group_id = 23082 WHERE id = 23073;

-- 4.Создайте несколько учебных предметов (subjects)

INSERT INTO subjects (title) VALUES ('Math2026'), ('History2026'), ('Sport2026');

-- 5.Создайте по два занятия для каждого предмета (lessons)

INSERT INTO lessons (title, subject_id)
VALUES ('lesson1', 23196), ('lesson2', 23196), ('lesson1', 23197),
('lesson2', 23197),('lesson1', 23198), ('lesson2', 23198);

-- 6.Поставьте своему студенту оценки (marks) для всех созданных вами занятий

INSERT INTO marks (value, lesson_id, student_id)
VALUES ('10', 76494, 23073), ('9', 76495, 23073), ('8', 76496, 23073), ('7', 76497, 23073),
('6', 76498, 23073), ('5', 76499, 23073);

-- Получите информацию из базы данных:

-- 1.Все оценки студента

SELECT * FROM marks WHERE student_id = 23073;

-- 2.Все книги, которые находятся у студента

SELECT * FROM books WHERE taken_by_student_id = 23073;

-- 3.Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий
-- и предметов (всё одним запросом с использованием Join)

SELECT * FROM students s JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m  ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects s2 ON l.subject_id = s2.id
WHERE s.id = 23073;