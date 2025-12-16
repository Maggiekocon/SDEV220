import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor() # represents connection with database, says run this in the database
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")
cur.execute("INSERT INTO users (username, password) VALUES ('admin','password123')") # stores password as plaintext
conn.commit()

print("Database ready.")


#writing the login feature
username = input("Enter username: ")
password = input("Enter password: ")
query=f"SELECT * From users WHERE username = ? AND password = ?" # Parameterize query
cur.execute(query, (username, password))

result = cur.fetchone()
if result:
    print("User Exists")
else:
    print("User does not Exist")

conn.close()

