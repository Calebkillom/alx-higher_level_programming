#!/usr/bin/python3
""" script that changes the name of a State object from the database """
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

    """ Querying the State object with id = 2 """
    state = session.query(State).filter_by(id=2).first()

    """ Check if the state is empty if not change and commit changes """
    if state is None:
        print("State with id = 2 not found")
    else:
        state.name = "New Mexico"
        session.commit()

    """ Closing the session """
    session.close()
