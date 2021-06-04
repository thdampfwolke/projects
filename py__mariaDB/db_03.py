#!/usr/bin/python3

"""
    https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/
    https://github.com/datacharmer/test_db
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
        database="employees"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

print(cur)
