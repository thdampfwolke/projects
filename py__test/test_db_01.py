#!/usr/bin/python3
# https://dzone.com/articles/python-to-mariadb-connector
# https://github.com/datacharmer/test_db

import mariadb
import sys

# Connect to MariaDB Platform
try: conn = mariadb.connect(
    user="django",
    password="password",
    host="127.0.0.1",
    port=3306,
    database="db_sap_03"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
print(dir(cur))
print(cur)

cur.execute(
    "SELECT id, nname, vname, geb FROM app_test_staff"
    )

# Print Result-set
for (id, nname, vname, geb) in cur:
    print(f"ID: {id}, NN: {nname}, VN: {vname}, GEB: {geb}")


#insert information
try:
    cur.execute("INSERT INTO app_test_staff (nname, vname) VALUES (?, ?, ?)", ("nname-03", "vname-03", 1))
    #cur.execute("INSERT INTO app_test_staff (nname, vname, check) VALUES ("nname-03", "vname-03", 1)")
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")

conn.close()




"""
# Adding Data
cursor.execute(
    "INSERT INTO employees (first_name,last_name) VALUES (?, ?)", 
    (first_name, last_name))

# Catching Exceptions
try: 
    cursor.execute("some MariaDB query")
except mariadb.Error as e: 
    print(f"Error: {e}")

# Close Connection
conn.close()

# commit()
# rollback()
# lastrowid()
"""
