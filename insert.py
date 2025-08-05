import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "root",
    database = "python"
)

print("Connected to the database")

query = "insert into student(name,email) values('Rajdeep Rangra','rajdeep@lawsikho.in')"

cursor = conn.cursor()
cursor.execute(query)     # execute the insert query
conn.commit()             # correct: commit on connection, not cursor
print("Data inserted successfully")

# Fetch and display all data
select_query = "SELECT * FROM student"
cursor.execute(select_query)
results = cursor.fetchall()

cursor.close()
conn.close()