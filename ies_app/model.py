from flask_sqlalchemy import SQLAlchemy

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