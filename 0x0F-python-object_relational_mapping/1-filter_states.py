#!/usr/bin/python3

"""
script that lists all states with a name starting with N (upper N)
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    argument passing
    """
    user_name = argv[1]
    db_name = argv[3]

    """
    connecting to the MySQL database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        password=argv[2],
        db=db_name
    )
    """
    creating a cursor to interact with the database
    """
    cursor = db.cursor()
    """
    executing the sql queries
    """
    cursor.execute("SELECT * FROM states WHERE UPPER(name) LIKE"
                   " 'N%' ORDER BY id ASC;")
    """
    fetching values from the result
    """
    result = cursor.fetchall()
    for value in result:
        print(value)
    """
    commiting changes and closing connection
    """
    db.commit()
    cursor.close()
    db.close()
