import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
print("Connected", conn)
cursor = conn.cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to", record)




# Closing database connection.
if(conn):
    cursor.close()
    conn.close()
    print("PostgreSQL connection is closed")



