#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the database """
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
                                   database_name))

    """ Creating a session factory """
    Session = sessionmaker(bind=engine)

    """ Creating a session """
    session = Session()

    """ Creating a new State object """
    new_state = State(name="Louisiana")

    """
    Add the new state to the session and commit the changes to the database
    """
    session.add(new_state)
    session.commit()

    """ Printing the new state's id """
    print(new_state.id)

    """ Closing the session """
    session.close()
