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
            CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            salary INT,
            department VARCHAR(50)
         )
         """
cursor.execute(create_table_query)
print("table 'employees' created successfully.")
insert_query="""
        INSERT INTO employees (name, salary, department)
        VALUES (%s, %s, %s)
        """
student_records= [
    ('alice',70000,'software engineer'),
    ('bob',65000,'assistent manager'),
    ('charlie',55000,'project manager')
    ]
cursor.executemany(insert_query,student_records)
connection.commit()
print(f"{cursor.rowcount}records inserted into 'employees' table.")


