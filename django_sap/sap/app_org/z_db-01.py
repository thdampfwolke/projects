#!/usr/bin/python3

"""
    https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/
    https://mariadb.com/docs/features/mariadb-connectors/
    https://mariadb.com/docs/clients/connector-python/#connector-python
    https://mariadb.com/docs/reference/conpy/api/#conpy-api
    https://github.com/datacharmer/test_db
    # id, nname, vname, is_staff, is_active
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
# insert information  -  # id, nname, vname, is_staff, is_active
try:
    cur.execute("INSERT INTO tab_user (nname,vname,is_staff,is_active) VALUES (?,?,?,?)",
                ("nname-01", "vname-01", True, True))
    cur.execute("INSERT INTO tab_user (nname,vname,is_staff,is_active) VALUES (?,?,?,?)",
                ("nname-02", "vname-02", True, False))
    cur.execute("INSERT INTO tab_user (nname,vname,is_staff,is_active) VALUES (?,?,?,?)",
                ("nname-03", "vname-03", False, True))
    cur.execute("INSERT INTO tab_user (nname,vname,is_staff,is_active) VALUES (?,?,?,?)",
                ("nname-04", "vname-04", False, False))
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")
# ----------------------------------------------------------------------------
"""


# ----------------------------------------------------------------------------
# retrieving information
abfrage = "vname-01"
cur.execute(
    "SELECT id, nname, vname, is_staff, is_active FROM tab_user WHERE vname=?", (abfrage,))

for id, nname, vname, is_staff, is_active in cur:
    print(id, nname, vname, is_staff, is_active)
print("-" * 50)

# -----------------------------------------------
cur.execute("SELECT id, nname, vname, is_staff, is_active FROM tab_user")

for id, nname, vname, is_staff, is_active in cur:
    print(id, nname, vname, is_staff, is_active, sep=';')
print("-" * 50)

# -----------------------------------------------
cur.execute("SELECT * FROM tab_user")

for i in cur:
    print(i)
print("-" * 50)

# ----------------------------------------------------------------------------

conn.close()
