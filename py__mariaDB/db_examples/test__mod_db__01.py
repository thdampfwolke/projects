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
# Basic Operations: add a single row to the table
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
# Basic Operations: add multiple rows to the table
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
# Basic Operations: Selecting Data
    deb = 0
    if deb == 1:
        mod_db.print_contacts(cur)

# ----------------------------------------------------------------------------
# Basic Operations: Replacing Data
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
# Basic Operations: Updating Data
    deb = 0
    if deb == 1:
        update_contact_email = "jrr.tolkien@example.edu"
        update_contact_lname = "Tolkien the Grey"

        mod_db.update_contact_last_name(
            cur, update_contact_email, update_contact_lname)
        conn.commit()

# ----------------------------------------------------------------------------
# Basic Operations: Deleting Data
    deb = 0
    if deb == 1:
        remove_contact_email = "jrr.tolkien@example.edu"
        mod_db.remove_contact(cur, remove_contact_email)
        conn.commit()

# ----------------------------------------------------------------------------
# Basic Operations: Truncating Data - inhalt von tab vollstaendig loeschen
    deb = 0
    if deb == 1:
        mod_db.truncate_contacts(cur)
        conn.commit()


# ----------------------------------------------------------------------------
# Transactions: Adds account
# Transactions: Update Last Name
#
# These function calls should succeed without any issues, so the transaction will be committed

    deb = 0
    if deb == 1:
        try:
            new_account_fname = "John"
            new_account_lname = "Rockefeller"
            new_account_email = "john.rockefeller@example.com"
            new_account_amount = 418000000000.00

            add_account(cur,
                        new_account_fname,
                        new_account_lname,
                        new_account_email,
                        new_account_amount)

            new_account_change = 1000000.00

            mod_db.update_account_amount(cur,
                                         new_account_email,
                                         new_account_change)

            conn.commit()

        except Exception as e:
            print(f"err: main: commiting transaction: {e}")
            conn.rollback()


# ----------------------------------------------------------------------------
# Transactions: Adds account
# Transactions: Update Last Name
#
# These function calls will fail due to the CHECK constraint.
# The account has an amount of 0.50, which the UPDATE statement attempts
# to reduce to -0.50, which is an invalid amount.
# The transaction fails and is rolled by with an error message

    deb = 0
    if deb == 1:

        try:
            new_account_fname = "Charlie"
            new_account_lname = "Bucket"
            new_account_email = "charlie.bucket@example.com"
            new_account_amount = 0.50

            mod_db.add_account(cur,
                               new_account_fname,
                               new_account_lname,
                               new_account_email,
                               new_account_amount)

            new_account_change = 1.00

            mod_db.update_account_amount(cur,
                                         new_account_email,
                                         new_account_change)

            conn.commit()
        except Exception as e:
            print(f"err: main: commiting transaction: {e}")
            conn.rollback()

# ============================================================================
# open:
# Connection Pooling:
#   Getting Connections from the Pool
#   Returning Connections to the Pool
#   Adding Existing Connections to the Pool
#   Reconfiguring Connection Pools
# ----------------------------------------------------------------------------


# ============================================================================
# Field Information:
#   Retrieving Field Information for Query Results
#   Retrieving Field Information for All Tables
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Field Information: Print List of Contacts
# Field Information: Get field info from cursor

    deb = 0
    if deb == 1:
        try:
            mod_db.select_contacts(cur)

            field_info = mariadb.fieldinfo()
            field_info_text = mod_db.get_field_info(cur, field_info)

            print("Columns in query results:")
            print("\n".join(field_info_text))
        except Exception as e:
            print(f"err: main: {e}")

# The results should look like this:
#   Columns in query results:
#   first_name: VAR_STRING
#   last_name:  VAR_STRING
#   email:      VAR_STRING


# ----------------------------------------------------------------------------
    deb = 1
    if deb == 1:
        try:
            mod_db.test_db(cur)
        except Exception as e:
            print(f"err: main: {e}")


# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

# ----------------------------------------------------------------------------
    deb = 0
    if deb == 1:
        pass

    # print(conn)
    # conn.commit()
    conn.close()
