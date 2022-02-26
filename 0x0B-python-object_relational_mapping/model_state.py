#!/usr/bin/python3
"""this module conmtains state class
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(base):
    """this is the state class
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True-, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
