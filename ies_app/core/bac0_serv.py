import BAC0 
                                                 #библиотека определения BACnet устройств в сети используя UDP
from ies_app.model import db, Data_controller                #из файла model.py импортируется БД для записи
from datetime import datetime                                #библиотека определения времени
from sqlalchemy.orm.session import sessionmaker
import os

bacnet = BAC0.connect(ip='192.168.0.10')                     #ip адрес хоста


controller = BAC0.device('192.168.0.90', 127001, bacnet, poll=0)     #ip адрес бакнет устройства



def get_datas():
        for point in controller.points:
                name_point = point.properties.name                   
                description_point = point.properties.description       
                value_point = point.value
                time_save = datetime.now()
                new_datas = Data_controller(name_point=name_point,description_point=description_point,\
                time_save=time_save,value_point=value_point)
                db.session.add_all(new_datas)
        db.session.commit()                                             # запись данных в БД

