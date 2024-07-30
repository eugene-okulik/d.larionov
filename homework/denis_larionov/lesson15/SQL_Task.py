import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
#
cursor = db.cursor(dictionary=True)
# cursor.execute('select * from students')
# print(cursor.fetchall())
#
# Создаем студента
cursor.execute("INSERT into students (name, second_name) values ('Maks2', 'Fray2')")
id_new_student = cursor.lastrowid
print(id_new_student)
# Создаем группу
cursor.execute("INSERT into `groups` (title, start_date, end_date) values ('Labirint', 'julie 2012', 'julie 2015')")
id_group = cursor.lastrowid
print(id_group)
# Вносим студента в созданную группу
cursor.execute(f"UPDATE students set group_id = {id_group} WHERE id = {id_new_student}")
# Создаем книги
cursor.execute(f"""INSERT INTO books (title, taken_by_student_id) values 
    ('cool_book', {id_new_student}),
    ('fantasy_book', {id_new_student})""")
# Создаем несколько учебных предметов
cursor.execute("INSERT into subjets (title) values ('astrology')")
id_subj_astr = cursor.lastrowid
print(id_subj_astr)
#
cursor.execute("INSERT into subjets (title) values ('mathematics')")
id_subj_math = cursor.lastrowid
print(id_subj_math)
# Создаем занятия для учебных предметов
cursor.execute(f"INSERT into lessons (title, subject_id) values ('Mars', {id_subj_astr})")
id_les_mars = cursor.lastrowid
print(id_les_mars)
#
cursor.execute(f"INSERT into lessons (title, subject_id) values ('functions', {id_subj_math})")
id_les_fun = cursor.lastrowid
print(id_les_fun)
# Проставляем оценки по предметам
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values (5, {id_les_mars}, {id_new_student})")
id_marks_mars = cursor.lastrowid
print(id_marks_mars)
#
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values (5, {id_les_mars}, {id_new_student})")
id_marks_fun = cursor.lastrowid
print(id_marks_fun)
#
#
#
# Выгружаем все оценки студена
cursor.execute(f"select value from marks where student_id = {id_new_student}")
print(cursor.fetchall())
# Выгружаем все книги, которые у студента
cursor.execute(f"SELECT title from books WHERE taken_by_student_id = {id_new_student}")
print(cursor.fetchall())
# Выводим все по студенту из БД
cursor.execute(f"""SELECT * from `groups` g join students s on
(g.id = s.group_id) join books b on
(b.taken_by_student_id = s.id) join marks m on
(s.id = m.student_id) join lessons l on
(m.lesson_id = l.id) join subjets s2 on
(s2.id = l.subject_id) where s.id = {id_new_student}""")
print(cursor.fetchall())
db.commit()
db.close()
