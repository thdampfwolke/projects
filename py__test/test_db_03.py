#!/usr/bin/python
# https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/

import mariadb

conn = mariadb.connect(
    user="django",
    password="password",
    host="127.0.0.1",
    database="employees")

cur = conn.cursor()

#retrieving information
some_name = "Georgi"
cur.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,))

for first_name, last_name in cur:
    print(f"First name: {first_name}, Last name: {last_name}")

#insert information
try:
    cur.execute("INSERT INTO employees (emp_no, first_name,last_name) VALUES (?, ?, ?)", (2, "Maria","DB"))
except mariadb.Error as e:
    print(f"-1- Error: {e}")

conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")

conn.close()
