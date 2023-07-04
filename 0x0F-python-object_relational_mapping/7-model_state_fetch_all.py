#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa """
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

    """ Querying all State objects and sorting by id in ascending order """
    states = session.query(State).order_by(State.id).all()

    """ Displaying the results """
    for state in states:
        print(f"{state.id}: {state.name}")

    """ Closing the session """
    session.close()
