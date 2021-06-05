#!/usr/bin/python3

# -----------------------------------------------
# Adds contact
def add_contact(cur, first_name, last_name, email):
    """Adds the given contact to the contacts table"""

    cur.execute("INSERT INTO db_test_mariadb.contacts(first_name, last_name, email) VALUES (?, ?, ?)",
                (first_name, last_name, email))


# -----------------------------------------------
# Add Multiple Rows
def add_multiple_contacts(cur, data):
    """Adds multiple contacts to database from given data"""

    cur.executemany(
        "INSERT INTO db_test_mariadb.contacts(first_name, last_name, email) VALUES (?, ?, ?)", data)


# -----------------------------------------------
# Print List of Contacts
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
