import mysql.connector
conn =mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "root",
    database = "python"
)

cursor = conn.cursor()
print("Connected to the database")
query = "select * from  student"
cursor.execute(query)  # execute the update query
results = cursor.fetchall()
for row in results:
    print("student name is ",row[1])  # Print each row of the result set
    print("student email is ",row[2])  # Print each row of the result set
    print()
print("Data fetched successfully")
cursor.close()
conn.close()

