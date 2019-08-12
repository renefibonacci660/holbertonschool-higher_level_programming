#!/usr/bin/python3
'''
    Prints the first State object from the database
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    eng = create_engine(connection.format(user, passwd, db),
                        pool_pre_ping=True)

    item = sessionmaker(bind=eng).query(State).first()

    if item is None:
        print("Nothing")
    else:
        print("{}: {}".format(item.id, item.name))
