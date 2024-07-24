INSERT into `groups` (title, start_date, end_date) values ('Qiwi', 'june 2010', 'jule 2024');
select * from `groups` g where id = 1550;
INSERT into students (name, second_name, group_id) values ('Qiwi', 'Pticsa', 1550);
select * from students WHERE name LIKE 'Qi%';
SELECT * from books where taken_by_student_id = 1629;
INSERT INTO books (title, taken_by_student_id) values
('Qiwi_lol', 1620),
('Qiwi_work', 1620),
('Qiwi_Fiscal', 1620);
SELECT * from subjets order by id desc;
SELECT * from subjets where title in ('SQL_tech', 'Menegment');
INSERT INTO subjets (title) values ('SQL_tech'), ('Menegment');
select * from lessons WHERE subject_id in (2069, 2070);
INSERT INTO lessons (title, subject_id)
values
('Lessons1_mgt', 2069),
('Lessons2_mgt', 2069),
('Lessons1_SQL', 2070),
('Lessons2_SQL', 2070);
select id from students WHERE name = 'Qiwi';
SELECT * from marks where student_id = 1629;
INSERT INTO marks (value, lesson_id, student_id) values 
(5, 4624, (select id from students WHERE name = 'Qiwi')),
(5, 4625, (select id from students WHERE name = 'Qiwi')),
(5, 4626, (select id from students WHERE name = 'Qiwi'));


select value from marks where student_id = 1620;
SELECT title from books WHERE taken_by_student_id = 1620;
SELECT * from `groups` g join students s on
(g.id = s.group_id) join books b on
(b.taken_by_student_id = s.id) join marks m on
(s.id = m.student_id) join lessons l on
(m.lesson_id = l.id) join subjets s2 on
(s2.id = l.subject_id) where s.id = 1629;

INSERT INTO students (name, second_name) values ('Qiwi2', 'Pticsa2');
UPDATE students set group_id = 1550 where id = 1629;
select * from students s WHERE id = 1629;

