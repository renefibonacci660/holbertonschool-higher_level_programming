#!/usr/bin/python3
'''
    changes the name of a State object from the database
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
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter_by(id=2).first()
    query.name = "New Mexico"
    session.commit()
