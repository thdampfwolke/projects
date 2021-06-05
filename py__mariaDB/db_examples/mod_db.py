#!/usr/bin/python3

# -----------------------------------------------
# add a single row to the table

def add_contact(cur, first_name, last_name, email):
    """Adds the given contact to the contacts table"""

    cur.execute("INSERT INTO db_test_mariadb.contacts(first_name, last_name, email) VALUES (?, ?, ?)",
                (first_name, last_name, email))


# -----------------------------------------------
# add multiple rows to the table

def add_multiple_contacts(cur, data):
    """Adds multiple contacts to database from given data"""

    cur.executemany(
        "INSERT INTO db_test_mariadb.contacts(first_name, last_name, email) VALUES (?, ?, ?)", data)


# -----------------------------------------------
# Selecting Data

def print_contacts(cur):
    """Retrieves the list of contacts from the database and prints to stdout"""

    # Initialize Variables
    contacts = []

    # -----------------------------------------------
    # Retrieve Contacts
    cur.execute(
        "SELECT id, first_name, last_name, email FROM db_test_mariadb.contacts")

    # Prepare Contacts
    for (id, first_name, last_name, email) in cur:
        contacts.append(f"{id};{first_name};{last_name};{email}")

    # print(type(cur))        ->   <class 'mariadb.connection.cursor'>
    # print(type(contacts))   ->   <class 'list'>

    # List Contacts
    print("\n".join(contacts))  # -> 2;J. R. R.;Tolkien;jrr.tolkien@example.edu

    # -----------------------------------------------
    cur.execute("SELECT * FROM db_test_mariadb.contacts")
    print("-" * 50)
    for i in cur:
        print(i)        # -> (2, 'J. R. R.', 'Tolkien', 'jrr.tolkien@example.edu')


# -----------------------------------------------
# Replacing Data

def replace_contact(cur, contact_id, first_name, last_name, email):
    """Replaces contact with the given `contact_id` with new values"""

    cur.execute("REPLACE INTO db_test_mariadb.contacts VALUES (?, ?, ?, ?)",
                (contact_id, first_name, last_name, email))


# -----------------------------------------------
# Updating Data

def update_contact_last_name(cur, email, last_name):
    """Updates last name of a contact in the table"""

    cur.execute("UPDATE db_test_mariadb.contacts SET last_name=? WHERE email=?",
                (last_name, email))


# -----------------------------------------------
# Deleting Data

def remove_contact(cur, email):
    """Removes contacts from the database"""

    cur.execute(
        "DELETE FROM db_test_mariadb.contacts WHERE email = ?", (email, ))


# -----------------------------------------------
# Truncating Data - inhalt von tab vollstaendig loeschen

def truncate_contacts(cur):
    """Removes all data from contacts table"""

    cur.execute("TRUNCATE db_test_mariadb.contacts")
