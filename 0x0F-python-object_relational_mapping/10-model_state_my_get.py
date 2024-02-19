#!/usr/bin/python3
"""
Sqlalchemy query of database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MY_USER = argv[1]
MY_PASS = argv[2]
MY_DB = argv[3]
STATE_NAME = argv[4]

if __name__ == "__main__":
    # create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(MY_USER,
                           MY_PASS, MY_DB), pool_pre_ping=True)

    # create session object and instance
    Session_factory = sessionmaker(bind=engine)
    session = Session_factory()

    # query and display result
    result = session.query(State).filter(State.name == STATE_NAME)

    if result.count() == 0:  # checking for empty query
        print("Not Found")
    else:
        for row in result:
            print("{}: {}".format(row.id, row.name))
