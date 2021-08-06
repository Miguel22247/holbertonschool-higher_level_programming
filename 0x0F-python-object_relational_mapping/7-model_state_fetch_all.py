#!/usr/bin/python3
"""A script that lists all states"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    if len(argv) != 4:
        print("error")
    else:
        USER = argv[1]
        PWD = argv[2]
        DB = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                .format(USER, PWD, DB), pool_pre_ping=True)
        
        Base.metadata.create_all(engine)
        
        Session = sessionmaker(bind=engine)
        session = Session()
        for states in session.query(State):
            print("{}: {}".format(states.id, states.name))
