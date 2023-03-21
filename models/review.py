#!/usr/bin/python3
"""Module of Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    ''' place_id will be the same as Place.id'''
    place_id = ''
    ''' user_id will be the same as User.id'''
    user_id = ''
    text = ''
