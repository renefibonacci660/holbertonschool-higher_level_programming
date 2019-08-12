#!/usr/bin/python3
'''
    Defines State ORM object by using SQLAlchemy
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):

    '''
        City ORM class that inherits from Base
        links to MySQL table "states"
        id = class attribute representing column of an auto generated
            unique integer that cannot be null & is primary key
        name = class attribute that represents str with max 128 char & !NULL
    '''

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
