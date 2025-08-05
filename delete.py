import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python"
)

cursor = conn.cursor()
print("Connected to the database")  
query = "DELETE FROM student WHERE id = 2"
cursor.execute(query)  # execute the delete query
conn.commit()        # commit the changes to the database
print("Data deleted successfully")

cursor.close()
conn.close()