#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """ MySQL connection parameters """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """ Creating the SQLAlchemy engine to connect to the MySQL server """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name), pool_pre_ping=True)

    """ Creating a session factory """
    Session = sessionmaker(bind=engine)

    """ Creating a session """
    session = Session()

    """ Querying all State objects with names containing the letter 'a' """
    states = session.query(State).filter(State.name.like('%a%')).all()

    """ Deleting the selected state objects """
    for state in states:
        session.delete(state)

    """ Commiting the changes to the database """
    session.commit()

    """ Closing the session """
    session.close()
