#!/usr/bin/python3

import mariadb
import sys
import mod_cmdb

deb = 0

if __name__ == "__main__":

    try:
        conn = mariadb.connect(
            user="django",
            password="password",
            host="127.0.0.1",
            # autocommit=True
            port=3306)
    except mariadb.Error as e:
        print(f"err: main: Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()

# ----------------------------------------------------------------------------
# db: tab: - id, name, ip

    deb = 0
    if deb == 1:
        mod_cmdb.select_server(cur)

# ----------------------------------------------------------------------------
# db: tab: - id, name, ip

    deb = 0
    if deb == 1:
        new_server = [
            ("srv-01", "1.1.1.1"),
            ("srv-02", "1.1.1.2"),
            ("srv-03", "1.1.1.3")
        ]

        mod_cmdb.add_server(cur, new_server)
        conn.commit()

# select * from db_test_cmdb.server;
