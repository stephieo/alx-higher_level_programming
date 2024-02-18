#!/usr/bin/python3
""" This module  contains the class definition of a State class that maps to the rows in the States table"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

    
#create base
Base = declarative_base()

#create State class
class State(Base):
    """definition of the class/model/table `State`"""
    __tablename__ = "states"

    id = Column("id",Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False, )

    

