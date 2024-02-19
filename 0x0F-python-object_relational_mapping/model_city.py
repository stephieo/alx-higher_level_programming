#!/usr/bin/python3
"""
 This module  contains the class definition of a City
 class that maps to the rows in the Cities table
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ class definition of City class/table"""

    __tablename__ = "cities"

    id = Column("id", Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer,
                      ForeignKey("states.id"), nullable=False, )
