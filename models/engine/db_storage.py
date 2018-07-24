#!/usr/bin/python3
"""DBStorage class that sets up SQLAlchemy and connects with database"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from base_model import Base
from user import User
from state import State
from city import City
from amenity import Amenity
from place import Place
from review import Review
from models import classes


class DBStorage:
    """
    DBStorage class
    """
    __engine = None
    __session = None

    def __init__self(self):
        """
        Initializes database connection
        """
        user_name = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user_name, pwd, host, db), pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Retrieves dictionary of objects in database
        Args:
            cls (obj): class of objects to be queried
        Returns:
            dictionary of objects
        """
        self.__session = sessionmaker(bind=self.__engine)
        session = self.__session()

        objs_dict = {}
        objs = None

        if cls:
            if cls in classes:
                objs = session.query(cls).all()
        else:
            objs = session.query(
                User, State, City, Amenity, Place, Review).all()
        for obj in objs:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            objs_dict[key] = obj

        return objs_dict
