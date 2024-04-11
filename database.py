import mysql.connector

# Establish connection to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUsu12345",
    database="med"
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

def search_db(string):
    cursor.execute(string)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()