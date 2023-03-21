#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
