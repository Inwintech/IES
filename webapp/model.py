# модель БД для bac0
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Datas(db.Model):
    id = db.Column(db.Integer, primary_key=True)             #id записи
    device = db.Column(db.String, nullable=False)            #имя контроллера
    description = db.Column(db.String, nullable=False)       #описание переменной
    published = db.Column(db.DateTime, nullable=False)       #время записи
    value = db.Column(db.Float, nullable=False)              #значение переменной

    