#!/usr/bin/python3
"""A script that lists all states"""

if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(argv) != 4:
        print("error")
    else:
        USER = argv[1]
        PASS = argv[2]
        DB = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(USER, PASS, DB), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        state_id = session.query(State).filter(State.name==argv[4]).first()
        if state_id:
            print(state_id[0].id)
        else:
            print("Not found")
        session.close()
