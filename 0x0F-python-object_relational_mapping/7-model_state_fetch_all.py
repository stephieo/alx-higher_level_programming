#!/usr/bin/python3
"""
This module is a script to query all State objects
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

MY_USER = argv[1]
MY_PASS = argv[2]
MY_DB = argv[3]

if __name__ == "__main__":
    # create the engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    # create session object and instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query table
    result = session.query(State).order_by(State.id)

    for row in result:
        print("{}: {}".format(row.id, row.name))
