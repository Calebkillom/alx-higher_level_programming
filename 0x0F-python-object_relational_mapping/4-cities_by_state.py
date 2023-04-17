#!/usr/bin/python3

"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    user_name = argv[1]
    pass_word = argv[2]
    db_name = argv[3]
    """
    connection to MySQLdb
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=pass_word,
        db=db_name)
    """
    creating cursor object to interact with the database
    """
    cursor = db.cursor()

    sql_query = "SELECT cities.id, cities.name, states.name FROM states\
        JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC;"

    cursor.execute(sql_query)
    result = cursor.fetchall()

    for value in result:
        print(value)
    """
    commiting changes and closing connection
    """
    db.commit()
    cursor.close()
    db.close()
