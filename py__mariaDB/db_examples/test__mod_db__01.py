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
    deb = 0
    if deb == 1:
        new_contact_fname = "J. R. R."
        new_contact_lname = "Tolkien"
        new_contact_email = "jrr.tolkien@example.edu"

        mod_db.add_contact(cur, new_contact_fname,
                           new_contact_lname, new_contact_email)
        conn.commit()

# select * from contacts;
# ----------------------------------------------------------------------------
    deb = 0
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
    deb = 0
    if deb == 1:
        mod_db.print_contacts(cur)

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        replace_contact_id = 1
        replace_contact_fname = "John Ronald Reuel"
        replace_contact_lname = "Tolkien"
        replace_contact_email = "jrr.tolkien@example.edu"

        mod_db.replace_contact(cur,
                               replace_contact_id,
                               replace_contact_fname,
                               replace_contact_lname,
                               replace_contact_email)
        conn.commit()

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        update_contact_email = "jrr.tolkien@example.edu"
        update_contact_lname = "Tolkien the Grey"

        mod_db.update_contact_last_name(
            cur, update_contact_email, update_contact_lname)
        conn.commit()

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        remove_contact_email = "jrr.tolkien@example.edu"
        mod_db.remove_contact(cur, remove_contact_email)
        conn.commit()

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        mod_db.truncate_contacts(cur)
        conn.commit()


# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass
# ----------------------------------------------------------------------------

    # print(conn)
    # conn.commit()
    conn.close()
