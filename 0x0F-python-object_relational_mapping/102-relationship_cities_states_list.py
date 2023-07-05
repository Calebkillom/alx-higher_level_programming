#!/usr/bin/python3
""" script that lists all City objects from the database """
import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ MySQL connection parameters """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """ Create the SQLAlchemy engine to connect to the MySQL server """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(mysql_username, mysql_password, database_name),
        pool_pre_ping=True)

    """ Creating the session factory and the session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query all City objects with their associated State objects """
    cities = session.query(City).join(State).order_by(City.id)

    """ Print the cities in the desired format """
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    """ Close the Session """
    session.close()
