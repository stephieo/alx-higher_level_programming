#!/usr/bin/python3
"""
module to create State classes
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

MY_USER = argv[1]
MY_PASS = argv[2]
MY_DB = argv[3]

# create the engine
engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(MY_USER, MY_PASS, MY_DB),
                       pool_pre_ping=True)
# create the classes that inherit from Base
Base.metadata.create_all(bind=engine)
