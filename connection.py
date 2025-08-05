import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user ="root",
    password = "root",
    database = "python"
)

query = "create table student(id int auto_increment PRIMARY KEY ,name varchar(50),email varchar(50))"
cursor = conn.cursor()

# Example query
cursor.execute(query)
conn.commit()


# Fetch and print result
# result = cursor.fetchone()
print("Table created")



# Close the connection
cursor.close()
conn.close()