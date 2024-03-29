#!/usr/bin/python3
"""
script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    argument passing
    """
    user_name = argv[1]
    pass_word = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    """
    connecting to the db
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=pass_word,
        db=db_name)
    """
    creating a cursor to interact with the database
    """
    cursor = db.cursor()
    """
    executing sql queries
    """
    thesql_query = "SELECT * FROM states WHERE name LIKE '%{}%'\
        ORDER BY id ASC".format(state_name)
    cursor.execute(thesql_query)

    """
    fetching all values from the result
    """
    result = cursor.fetchall()
    for value in result:
        print(value)
    """
    commiting changes and closing the connection
    """
    db.commit()
    cursor.close()
    db.close()
