#!/usr/bin/python3
'''
    Prints all City objects from the database
'''

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection.format(user, passwd, db),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)

    for each_state, each_city in session().\
            query(State, City).filter(City.state_id == State.id):
        print('{}: ({}) {}'.format(each_state.
                                   name, each_city.id, each_city.name))

    session().close()
