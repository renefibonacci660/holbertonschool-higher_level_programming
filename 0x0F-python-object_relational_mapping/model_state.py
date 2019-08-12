#!/usr/bin/python3
'''
    Defines State ORM object by using SQLAlchemy
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
        State ORM class that inherits from Base
        links to MySQL table "states"
        id = class attribute representing column of an auto generated
            unique integer that cannot be null & is primary key
        name = class attribute that represents str with max 128 char & !NULL
    '''

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
