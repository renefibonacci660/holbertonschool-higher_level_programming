#!/usr/bin/python3
'''
    Deletes all State objects with name containing letter a from database
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
    engine = create_engine(connection.format(user, passwd, db),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)

    query = session().query(State).filter(State.name.ilike("%a%")).all()
    for row in query:
        session().delete(row)
    session().commit()
