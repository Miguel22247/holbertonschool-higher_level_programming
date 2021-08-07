#!/usr/bin/python3
"""prints all the cities"""

if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(USER, PASS, DB), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for cities in session.query(City):
        for states in session.query(State).filter(State.id == cities.state_id):
            print("{}: ({}) {}".format(states.name, cities.id, cities.name))
