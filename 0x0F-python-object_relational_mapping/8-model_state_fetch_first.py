#!/usr/bin/python3
""" script that prints the first State object from the database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """ Connecting to the database using SQLAlchemy """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    """ Create a session factory """
    Session = sessionmaker(bind=engine)

    """ Creating a session """
    session = Session()

    """ Querying the first State object """
    state = session.query(State).order_by(State.id).first()

    """ Checking if state is None (empty table) """
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    """ Closing the session """
    session.close()
