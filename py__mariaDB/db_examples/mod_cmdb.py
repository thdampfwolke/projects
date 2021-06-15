#!/usr/bin/python3

# -----------------------------------------------
# mod_cmdb.add_server(cur, new_server: id, name, ip)

def add_server(cur, data):
    """adds server to db"""

    cur.executemany(
        "INSERT INTO db_test_cmdb.server(name, ip) VALUES (?, ?)", data
    )

# -----------------------------------------------
# mod_cmdb.select_server(cur)

def select_server(cur):
    # cur.execute("SELECT * FROM db_test_cmdb.server")
    cur.execute("SELECT id, name FROM db_test_cmdb.server")
    for f_i in cur:
        print(f_i)      # ->