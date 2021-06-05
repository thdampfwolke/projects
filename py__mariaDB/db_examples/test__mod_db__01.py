#!/usr/bin/python3

import mariadb
import sys
import mod_db

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
    if deb == 1:
        new_contact_fname = "J. R. R."
        new_contact_lname = "Tolkien"
        new_contact_email = "jrr.tolkien@example.edu"

        mod_db.add_contact(cur, new_contact_fname,
                           new_contact_lname, new_contact_email)
        conn.commit()

# select * from contacts;
# ----------------------------------------------------------------------------
    if deb == 1:
        new_contacts = [
            ("Howard", "Lovecraft", "hp.lovecraft@example.net"),
            ("Flannery", "O'Connor", "flan.oconnor@example.com"),
            ("Walker", "Percy", "w.percy@example.edu")
        ]

        mod_db.add_multiple_contacts(cur, new_contacts)
        conn.commit()

# select * from contacts;
# ----------------------------------------------------------------------------
    if deb == 1:
        mod_db.print_contacts(cur)

# ----------------------------------------------------------------------------
    deb = 0
# ----------------------------------------------------------------------------

    # print(conn)
    # conn.commit()
    conn.close()
