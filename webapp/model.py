# модель БД для bac0
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Datas(db.Model):
    id = db.Column(db.Integer, primary_key=True)             #id записи
    device = db.Column(db.String, nullable=False)            #имя контроллера
    description = db.Column(db.String, nullable=False)       #описание переменной
    published = db.Column(db.DateTime, default=datetime.utcnow)       #время пишется автоматически (время записи)
    value = db.Column(db.String, nullable=False)              #значение переменной

def __repr__(self):
    return '<Datas {} {}>'.format(self.description, self.value)
