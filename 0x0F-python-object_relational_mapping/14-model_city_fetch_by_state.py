#!/usr/bin/python3
"""
python script to print all records in cities database
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MY_USER = argv[1]
MY_PASS = argv[2]
MY_DB = argv[3]

if __name__ == "__main__":
    # create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    # create tables
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    sess14 = Session()

    results = sess14.query(State, City).filter(
              State.id == City.state_id).order_by(
              City.id).all()

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
