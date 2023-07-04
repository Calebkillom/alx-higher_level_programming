#!/usr/bin/python3
""" script that prints all City objects from the database hbtn_0e_14_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    """ Querying all City objects from the database """
    cities = session.query(City).order_by(City.id).all()

    """ Printing the cities """
    for city in cities:
        state_name = session.query(State).filter_by(id=city
                                                    .state_id).first().name
        print(f"{state_name}: ({city.id}) {city.name}")

    """ Closing the session """
    session.close()
