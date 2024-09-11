import mysql.connector

connection=mysql.connector.connect(
    host='localhost',
    database='sdp',
    user='root',
    password='root123'
)
if connection.is_connected():
    print("successfully connected to the database")
    cursor=connection.cursor()
    create_table_query= """
            CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT,
            gender VARCHAR(10)
         )
         """
cursor.execute(create_table_query)
print("table 'students' created successfully.")
insert_query="""
        INSERT INTO students (name, age, gender)
        VALUES (%s, %s, %s)
        """
student_records= [
    ('alice',22,'female'),
    ('bob',24,'male'),
    ('charlie',23,'male')
    ]
cursor.executemany(insert_query,student_records)
connection.commit()
print(f"{cursor.rowcount}records inserted into 'students' table.")


