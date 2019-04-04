import BAC0
from flask import current_app
from webapp.model import db, Datas

def get_datas():
    bacnet = BAC0.connect(ip=current_app.config['SERVER_IP'])
    bacnet.whois()
    bacnet.devices
    controller = BAC0.device(current_app.config['DEVICE_IP'], current_app.config['DEVICE_ID'], bacnet)
    for point in controller.points:
        value = point.value
        device = point.properties.name                   
        description = point.properties.description
        value = point.value       
        save_datas(device,description,value)

def save_datas(device,description,value):
    new_datas = Datas(device=device,description=description,value=value)
    db.session.add(new_datas)
    db.session.commit()
    
   
   
    #print(point.properties.name, point.properties.type, point.properties.description, point.value)

#if point.properties.type == 'analogInput' or point.properties.type == 'analogValue':
#    value = point.value
#else:
#    value = float(point.boolValue)

#with open('points.txt','w', encoding='utf-8') as f:
    #i=0
    #while i<1:
        #obj_list = bacnet.read('192.168.1.155 device 518083 objectList')
        #f.write(datetime.now().strftime('%d.%m.%Y %H:%M'))
        #f.write(str(controller.points))
        #for point in controller.points:
            #print(type(point))
            #print(dir(point)) #все доступные параметры для объекта Python
        

