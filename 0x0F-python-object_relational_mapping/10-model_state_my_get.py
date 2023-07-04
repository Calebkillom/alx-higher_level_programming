#!/usr/bin/python3
"""
script that prints the State object with
name passed as argument from the database
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
    state_name = sys.argv[4]

    """ Creating the SQLAlchemy engine to connect to the MySQL server """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    """ Create a session factory """
    Session = sessionmaker(bind=engine)

    """ Creating a session """
    session = Session()

    """ Querying the State object with the given state name """
    state = session.query(State).filter_by(name=state_name).first()

    """ Checking if the state is None/not found """
    if state is None:
        print("Not found")
    else:
        print(state.id)

    """ Closing the session """
    session.close()
