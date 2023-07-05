#!/usr/bin/python3
"""
script that lists all State objects,
corresponding City objects,
contained in the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """ MySQL connection parameters """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """ Creating the SQLAlchemy engine to connect to the MySQL server """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(mysql_username, mysql_password, database_name),
        pool_pre_ping=True)

    """ Create all tables in the engine """
    Base.metadata.create_all(engine)

    """ Create a session factory """
    Session = sessionmaker(bind=engine)

    """ Create a session """
    session = Session()

    """ Query all State objects with their corresponding City objects """
    states = session.query(State).order_by(State.id)

    """ Print the states and cities """
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    """ Closing the session """
    session.close()
