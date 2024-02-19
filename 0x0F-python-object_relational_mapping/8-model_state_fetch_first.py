#!/usr/bin/python3
"""
SQLAlchemy query to return first state object/row from database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

MY_USER = argv[1]
MY_PASS = argv[2]
MY_DB = argv[3]

if __name__ == "__main__":
    # create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    # create session object and instance
    Session_factory = sessionmaker(bind=engine)
    session = Session_factory()

    # query table and display results
    result = session.query(State).first()

    print("{}: {}".format(result.id, result.name))
