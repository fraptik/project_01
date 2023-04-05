# Самостоятельная работа №1

import sqlite3
connection = sqlite3.connect("teachers.db")
cursor = connection.cursor()
query = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL PRIMARY KEY,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL
);
"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect("teachers.db")
cursor = connection.cursor()
new_query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
('201', 'Иван', '1'),
('202', 'Петр', '2'),
('203', 'Анастасия', '3'),
('204', 'Игорь', '4');
"""
cursor.execute(new_query)
connection.commit()
connection.close()

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """select * FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Student_Id = ?"""
    cursor.execute(select_query,(student_id,))
    records = cursor.fetchall()
    close_connection(connection)
    for row in records:
      print ("ID Студента: ", row[0])
      print ("Имя студента: ", row[1])
      print ("ID школы: ", row[2])
      print ("Название школы: ", row[4], "\n")
  except (Exception, sqlite3.Erorr) as error:
    print ("Ошибка в получении данных", error)

print ("Самостоятельная работа №1. Написать программу, с помощью которой по ID студента можно получать информацию о школе и студенте.\n")
get_student(204)
