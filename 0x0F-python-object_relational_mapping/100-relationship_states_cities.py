#!/usr/bin/python3
""" script that creates the State “California” with “San Francisco” """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


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

    """ Creating all the tables in the database """
    Base.metadata.create_all(engine)

    """ Creating a session factory """
    Session = sessionmaker(bind=engine)

    """ Creating a session """
    session = Session()

    """ Creating the State object """
    california = State(name="California")

    """ Creating the City Object """
    san_francisco = City(name="San Francisco")

    """ Associating the City object with the State object """
    california.cities.append(san_francisco)

    """ Adding the State object to the session """
    session.add(california)

    """ Commiting the changes to the database """
    session.commit()

    """ Closing the session """
    session.close()
