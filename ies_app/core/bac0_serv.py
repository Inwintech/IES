import datetime
import BAC0                                                  #библиотека определения BACnet устройств в сети используя UDP
from flask import current_app                                # определение переменных из текущего приложения (в данном случае config)
from ies_app.model import db, Data_controller
import time                

bacnet = BAC0.connect(ip='192.168.0.10')

controller = BAC0.device('192.168.0.90', 127001, bacnet, poll=0)     #ip адрес бакнет устройства



def get_datas():
        start = time.time()
        for point in controller.points:
                name_point = point.properties.name                   
                description_point = point.properties.description       
                value_point = point.value
                time_save = datetime.datetime.now()
                save_datas = Data_controller(name_point = name_point, description_point = description_point, \
                                             value_point = value_point,time_save = time_save)
                db.session.add(save_datas)
                
        db.session.commit()
        duration = time.time() - start
        print (duration)                                          
