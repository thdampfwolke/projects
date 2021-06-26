import sys
import datetime
import mysql.connector
from mysql.connector import errorcode

# https://docs.python.org/3/tutorial/datastructures.html

try:
    cnx = mysql.connector.connect(
        user="root",
        password="asd123",
        host="127.0.0.1",
        # port=PORT,
        database="db_sap_test_bkp"
    )
    cursor = cnx.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

else:
    # -----------------------------------------------
    query = ("SELECT id_rolle, rolle_name FROM tab_rolle_new")
    cursor.execute(query)

    rolle = {}

    for a in cursor:
        print(a)
        rolle[a[0]] = a[1]

    print(rolle)

    for id, server in rolle.items():
        print(id, server)


    #print(sorted(rolle_list))
    #rolle_set = set(sorted(rolle_list))
    #print(sorted(rolle_set))

    #for b in (sorted(rolle_set)):
    #    #print(b)
    #    query = (f'insert into tab_rolle_new (rolle_name) values("{b}");')
    #    print(query)
    #    # cursor.execute(query)

   #for a in cursor:
   #    if a[2] == 'ansible':
   #        if a[3] == a[4]:
   #            id.append(a[0])

   ## -----------------------------------------------
   #for b in id:
   #    query = (f'UPDATE app_core_infra_server SET is_main_ip = 1 WHERE id = {b}')
   #    print(query)
   #    cursor.execute(query)

    # cnx.commit()
    cursor.close()
    cnx.close()