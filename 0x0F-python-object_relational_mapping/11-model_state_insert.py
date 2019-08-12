#!/usr/bin/python3
'''
    Adds the State object “Louisiana” to the specified database
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

    state_to_add = State(name="Louisiana")
    session().add(state_to_add)
    session().commit()
    obj = session().query(State).filter_by(name="Louisiana").first()
    print(obj.id)
