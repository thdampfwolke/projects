#!/usr/bin/python3

"""
https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/
https://github.com/datacharmer/test_db
https://github.com/mariadb-corporation/Developer-Examples?
/c/Program\ Files/MariaDB\ 10.5/bin/mysql.exe < employees.sql
"""

# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="django",
        password="password",
        host="127.0.0.1",
        port=3306,
        database="db_py"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
print(cur)


"""
# ----------------------------------------------------------------------------
import mariadb

conn = mariadb.connect(
    user="django",
    password="password",
    host="localhost",
    database="db_py")
cur = conn.cursor()

# retrieving information
some_name = "Georgi"
cur.execute(
    "SELECT first_name,last_name FROM db_py WHERE first_name=?", (some_name,))

for first_name, last_name in cur:
    print(f"First name: {first_name}, Last name: {last_name}")

# insert information
try:
    cur.execute(
        "INSERT INTO db_py (first_name,last_name) VALUES (?, ?)", ("Maria", "DB"))
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")

conn.close()
"""
