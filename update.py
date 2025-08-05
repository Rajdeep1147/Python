import mysql.connector
conn =mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "root",
    database = "python"
)

cursor = conn.cursor()
print("Connected to the database")
query = "update student set name ='Rocky Rangra' where id = 1"
cursor.execute(query)  # execute the update query
conn.commit()        # commit the changes to the database
print("Data updated successfully")

cursor.close()
conn.close()

