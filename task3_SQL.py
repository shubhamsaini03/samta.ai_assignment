import mysql.connector

# Create a MySQL connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="shubham",
    password="Shubham@123",
    database="student"
)

cursor = db_connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    grade FLOAT
)
"""
cursor.execute(create_table_query)
db_connection.commit()

insert_query = """
INSERT INTO students (first_name, last_name, age, grade)
VALUES (%s, %s, %s, %s)
"""
student_data = ("Alice", "Smith", 18, 95.5)
cursor.execute(insert_query, student_data)
db_connection.commit()

update_query = """
UPDATE students
SET grade = %s
WHERE first_name = %s
"""
updated_grade = 97.0
cursor.execute(update_query, (updated_grade, "Alice"))
db_connection.commit()

delete_query = """
DELETE FROM students
WHERE last_name = %s
"""
last_name_to_delete = "Smith"
cursor.execute(delete_query, (last_name_to_delete,))
db_connection.commit()

fetch_query = "SELECT * FROM students"
cursor.execute(fetch_query)
students = cursor.fetchall()

print("All Student Records:")
for student in students:
    print(student)

cursor.close()
db_connection.close()
