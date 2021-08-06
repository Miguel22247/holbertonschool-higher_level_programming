#!/usr/bin/python3
"""A script that lists all states"""

from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("error")
    else:
        USER = sys.argv[1]
        PWD = sys.argv[2]
        DB = sys.argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                .format(USER, PWD, DB), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        for instance in session.query(State).order_by(State.id):
            print("{}: {}".format(instance.id, instance.name))
