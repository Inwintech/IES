from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base() 
DBSession = scoped_session(sessionmaker()) 
engine = None

db = SQLAlchemy()

class Data_controller(db.Model):
    id = db.Column(db.Integer, primary_key=True)              #id записи
    name_point = db.Column(db.String, nullable=False)         #имя контроллера
    description_point = db.Column(db.String, nullable=False)  #описание переменной
    value_point = db.Column(db.String, nullable=False)        #значение переменной
    time_save = db.Column(db.DateTime, nullable=False)        #время записи
    
    def __repr__(self):
        return '<Data_controller {} {} {} {} {}>'.format(self.name_point, self.description_point,\
        self.value_point, self.time_save)
"""
def init_sqlalchemy(dbname='sqlite:///ies_1.db'): 
    global engine 
    engine = create_engine(dbname, echo=False) 
    DBSession.remove() 
    DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False) 
    Base.metadata.drop_all(engine) 
    Base.metadata.create_all(engine) 
"""