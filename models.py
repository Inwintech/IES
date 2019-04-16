from datetime import datetime              #нужна для того, чтобы писать время от сюда в базу данных
from app import db


class Data_controller(db.Model):
    __tablename__ = 'Data_controller'

    id = db.Column(db.Integer, primary_key=True)              #id записи
    name_point = db.Column(db.String, nullable=False)         #имя контроллера
    description_point = db.Column(db.String, nullable=False)  #описание переменной
    value_point = db.Column(db.String, nullable=False)        #значение переменной
    time_save = db.Column(db.DateTime, default=datetime.utcnow)        #время записи берется прям из этого модуля!
    
    def __repr__(self):
        return '<Data_controller {} {} {} {} {}>'.format(self.name_point, self.description_point,\
        self.value_point, self.time_save)