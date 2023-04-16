#!/usr/bin/python3

"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

"""
this statement is commonly used in Python scripts
that are intended to be both executable scripts
and reusable modules.
"""

if __name__ == "__main__":

    """
    connecting to the MySQLdb and providing the connection details.
    """

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    """
    creating a cursor to interact with the database
    """
    cursor = db.cursor()

    """
    using the cursor to execute sql queries
    """
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    result = cursor.fetchall()

    for row in result:
        print(row)

    """
    commiting changes and closing the connection.
    """
    db.commit()
    cursor.close()
    db.close()
