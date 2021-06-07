#!/usr/bin/python3

"""
    -------------------------------------------------
    Basic Operations:
    - add a single row to the table
    - add multiple rows to the table
    - Selecting Data
    - Replacing Data
    - Updating Data
    - Deleting Data
    - Truncating Data
    -------------------------------------------------
    Transactions: BEGIN, ROLLBACK, COMMIT
    - Adds account
    - Update Last Name
    -------------------------------------------------
    Connection Pooling:
    - Getting Connections from the Pool
    - Returning Connections to the Pool
    - Adding Existing Connections to the Pool
    - Reconfiguring Connection Pools

    -------------------------------------------------
    Field Information:
    - Retrieving Field Information for Query Results
    - Retrieving Field Information for All Tables

    -------------------------------------------------
"""

# -----------------------------------------------
# Basic Operations: add a single row to the table


def add_contact(cur, first_name, last_name, email):
    """Adds the given contact to the contacts table"""

    cur.execute("INSERT INTO db_test_mariadb.contacts(first_name, last_name, email) VALUES (?, ?, ?)",
                (first_name, last_name, email))


# -----------------------------------------------
# Basic Operations: add multiple rows to the table

def add_multiple_contacts(cur, data):
    """Adds multiple contacts to database from given data"""

    cur.executemany(
        "INSERT INTO db_test_mariadb.contacts(first_name, last_name, email) VALUES (?, ?, ?)", data)


# -----------------------------------------------
# Basic Operations: Selecting Data

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
# Basic Operations: Replacing Data

def replace_contact(cur, contact_id, first_name, last_name, email):
    """Replaces contact with the given `contact_id` with new values"""

    cur.execute("REPLACE INTO db_test_mariadb.contacts VALUES (?, ?, ?, ?)",
                (contact_id, first_name, last_name, email))


# -----------------------------------------------
# Basic Operations: Updating Data

def update_contact_last_name(cur, email, last_name):
    """Updates last name of a contact in the table"""

    cur.execute("UPDATE db_test_mariadb.contacts SET last_name=? WHERE email=?",
                (last_name, email))


# -----------------------------------------------
# Basic Operations: Deleting Data

def remove_contact(cur, email):
    """Removes contacts from the database"""

    cur.execute(
        "DELETE FROM db_test_mariadb.contacts WHERE email = ?", (email, ))


# -----------------------------------------------
# Basic Operations: Truncating Data - inhalt von tab vollstaendig loeschen

def truncate_contacts(cur):
    """Removes all data from contacts table"""

    cur.execute("TRUNCATE db_test_mariadb.contacts")


# -----------------------------------------------
# Transactions: Adds account

def add_account(cur, first_name, last_name, email, amount):
    """Adds the given account to the accounts table"""
    cur.execute("INSERT INTO db_test_mariadb.accounts(first_name, last_name, email, amount) VALUES (?, ?, ?, ?)",
                (first_name, last_name, email, amount))

# -----------------------------------------------
# Transactions: Update Last Name


def update_account_amount(cur, email, change):
    """Updates amount of an account in the table"""
    cur.execute("UPDATE db_test_mariadb.accounts SET amount=(amount-?) WHERE email=?",
                (change, email))

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


# -----------------------------------------------
# Field Information: Print List of Contacts
def select_contacts(cur):
    """Retrieves the list of contacts from the database"""

    # Retrieve Contacts
    cur.execute(
        "SELECT first_name, last_name, email FROM db_test_mariadb.contacts")

# -----------------------------------------------
# Field Information: Get field info from cursor


def get_field_info(cur, field_info):
    """Retrieves the field info associated with a cursor"""

    # field_info = mariadb.fieldinfo()
    field_info_text = []

    # Retrieve Column Information
    for column in cur.description:
        column_name = column[0]
        column_type = field_info.type(column)
        column_flags = field_info.flag(column)
        field_info_text.append(f"{column_name}: {column_type} {column_flags}")

    return field_info_text

    # -----------------------------------------------


def test_db(cur):
    cur.execute("desc db_test_mariadb.contacts")
    print("-" * 50)
    for i in cur:
        print(i)

    cur.execute("show create table db_test_mariadb.contacts")
    print("-" * 50)
    print(cur)
    print("-" * 50)
    for i in cur:
        print(f"{i}\n")

# -----------------------------------------------
# my: test: show databases


def test_db__show_databases(cur):
    print("-" * 79)
    cur.execute("show databases")

    f_db_list = []
    f_db_tab_list = []
    f_db_dic = {}

    for i in cur:
        print(f"{i}")
        f_db_list.append(i[0])

    # print(f_db_list)
    for i in f_db_list:
        f_db_tab_list = []
        print("-" * 50)
        print(f"01 - db  - {i}")
        cli = f"show tables in {i}"
        cur.execute(cli)
        for n in cur:
            print(f"02 - tab - {n}")
            f_db_tab_list.append(n[0])
        print(f_db_tab_list)
        f_db_dic[i] = f_db_tab_list

    for i in f_db_dic.items():      # fehler
        print(i)
        print(i[0] + ' \t - \t ' + i[1])
