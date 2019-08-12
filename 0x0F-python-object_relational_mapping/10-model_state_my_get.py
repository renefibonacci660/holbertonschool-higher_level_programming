#!/usr/bin/python3
'''
    Prints the State object with the name passed as argument from database
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    search = sys.argv[4]
    engine = create_engine(connection.format(user, passwd, db),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)

    query = (session().query(State).filter_by(name=search).
             order_by(State.id).all())

    if len(query) == 0:
        print("Not found")

    for item in query:
        print("{}".format(item.id))
