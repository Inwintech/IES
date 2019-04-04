import BAC0                                                  #библиотека определения BACnet устройств в сети используя UDP
from flask import current_app                                # определение переменных из текущего приложения (в данном случае config)
from ies_app.model import db, Data_controller                #из файла model.py импортируется БД для записи



def get_datas():                                                                  # функция подготовки переменой points 
    bacnet = BAC0.connect(ip=current_app.config['SERVER_IP'])                     #ip адрес хоста из config
    controller = BAC0.device(current_app.config['DEVICE_IP'], current_app.config['DEVICE_ID'], bacnet)     #ip адрес бакнет устройства из config
    for point in controller.points:                          # для записи в БД
        name_point = point.properties.name                   
        description_point = point.properties.description       
        value_point = point.value
        save_datas(name_point,description_point,value_point)
        

def save_datas(name_point,description_point,value_point):      # функция записи в БД 
    new_datas = Data_controller(name_point=name_point,description_point=description_point,\
    value_point=value_point)
    db.session.add(new_datas)                                     # добавление данных в БД 
    db.session.commit()                                           # запись данных в БД