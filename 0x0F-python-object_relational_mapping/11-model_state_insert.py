#!/usr/bin/python3
"""
Using Sqlalchemy to add record to  database
"""

from sys import argv 
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MY_USER = argv[1]
MY_PASS = argv[2]
MY_DB = argv[3]

if __name__ == "__main__":
    # create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(MY_USER, MY_PASS, MY_DB), pool_pre_ping=True)

    # create session object and instance
    Session_factory = sessionmaker(bind=engine)
    session = Session_factory()

    # 1.create object/record 2. add to database 3.commit changes
    s1 = State(name = 'Louisiana')
    session.add(s1)
    session.commit()

    #check for successful commit

    print(s1.id)
