#!/usr/bin/python3
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
    thesql_query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(thesql_query, (state_name,))

    """
    fetching all values from the result
    """
    result = cursor.fetchall()
    for value in result:
        if value[1] == state_name:
            print(value)
    """
    commiting changes and closing the connection
    """
    db.commit()
    cursor.close()
    db.close()
