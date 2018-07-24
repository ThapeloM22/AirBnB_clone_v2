#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer, Float
import os
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", passive_deletes=True, backref="place")
    else:
        @property
        def reviews(self):
            """
            """
            reviews_dict = models.storage.all(Review)
            reviews_list = []
            for review in reviews_dict.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
