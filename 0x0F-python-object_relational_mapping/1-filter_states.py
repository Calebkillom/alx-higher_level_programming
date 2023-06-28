#!/usr/bin/python3

"""
script that lists all states with a name starting with N (upper N)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Argument passing
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]

    # Connecting to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=password,
        db=db_name
    )

    # Creating a cursor to interact with the database
    cursor = db.cursor()

    # Executing the SQL queries
    cursor.execute("SELECT * FROM states WHERE UPPER(name)\
                   LIKE 'N%' ORDER BY id ASC; ")

    # Fetching values from the result
    result = cursor.fetchall()

    # Printing the results
    for value in result:
        print(value)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
