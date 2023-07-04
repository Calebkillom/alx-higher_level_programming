#!/usr/bin/python3
"""
File that contains the class definition of
State and an instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

""" Creating the declarative base instance """
Base = declarative_base()


class State(Base):
    """ class definition of a State """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
