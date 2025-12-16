1. 
import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).hexdigest()

def verify_password(password: str, stored_hash: str) -> bool:
    return hash_password(password) == stored_hash



# List at least three reasons this password storage approach is insecure.

# Explain what an attacker can do if they obtain the password hash database from this system.

# Replace this design with a more secure scheme using a modern password hashing library (for example, bcrypt or argon2) and briefly describe:

# How salts are handled

# How “work factor” / cost makes attacks more expensive

# Link this to the relevant OWASP category and name one OWASP cheat sheet that would help improve this code.

2. 

import sqlite3
from getpass import getpass

def login():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()

    username = input("Username: ")
    password = getpass("Password: ")

    query = f"SELECT * FROM users WHERE username = ? AND password = ?"
    cur.execute(query,(username, password))
    row = cur.fetchone()

    if row:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    conn.close()

if __name__ == "__main__":
    login()

# Identify the vulnerability in how the SQL query is built.

# Rewrite the login code using parameterized queries to prevent this vulnerability.
# Name the relevant OWASP Top 10 category and explain why this code is risky in a real application.
3.

import requests

variable = database.get(variable) # store key in a database
API_KEY = variable 
BASE_URL = "https://api.payment-provider.example/v1"

def charge_customer(customer_id, amount_cents):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"customer": customer_id, "amount": amount_cents}
    response = requests.post(f"{BASE_URL}/charge", headers=headers, json=data)
    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    cid = input("Customer ID: ")
    amt = int(input("Amount (cents): "))
    charge_customer(cid, amt)

# Explain why hardcoding API_KEY in the source code is a security problem.
# Describe what could happen if this repository is accidentally made public or sent to a contractor.
# Propose a more secure way to handle this API key in Python (hint: environment variables, config files, secret managers, etc.).
# Name at least one OWASP category this falls under (e.g., Cryptographic Failures, Security Misconfiguration, Software and Data Integrity Failures) and explain briefly.