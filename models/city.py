#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
import os

class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = 'cities'
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
