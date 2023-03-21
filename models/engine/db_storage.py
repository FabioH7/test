#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
import os


class DBStorage:
    __engine = None
    __session = None

    tables = {
        'State': State,
        'City': City
    }

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        # Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        metadata = MetaData(bind=self.__engine)

        if os.getenv('HBNB_ENV') == "test":
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        new_dict = {}
        name = DBStorage.tables[cls]
        all_obj = self.__session.query(name).all()
        for obj in all_obj:
            index = obj.to_dict()['__class__'] + '.' + obj.id
            new_dict[index] = obj
        return new_dict

    def new(self, obj):
        # table_name = DBStorage.tables[obj.__class__.__name__]
        new_row = DBStorage.tables[obj.__class__.__name__](**obj.to_dict())
        self.__session.add(new_row)
        self.save()

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            row = self.__session.query(DBStorage.tables[obj.__class__.__name__]).filter_by(
                id=obj.id)
            self.__session.delete(row)

    def reload(self):
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
        Base.metadata.create_all(self.__engine)
