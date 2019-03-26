import BAC0
from webapp.model import db, Datas
from datetime import datetime
import pandas as pd


bacnet = BAC0.connect(ip='192.168.1.104')
bacnet.whois()
bacnet.devices
controller = BAC0.device('192.168.1.155', 518083, bacnet)

print (bacnet.whois())
print (bacnet.devices)
print(controller)

def get_datas():
    for point in controller.points:
        device = point.properties.name                   
        description = point.properties.description       
        published = datetime.now()    
        value = point.value
        save_datas(device,description,published,value)

def save_datas(device,description,published,value):
    new_datas = Datas(device=device,description=description,published=published,value=value)
    db.session.add(new_datas)
    db.session.commit()

    #if point.properties.type == 'analogInput' or point.properties.type == 'analogValue':
        #print(point.value)
    #else:
        #print(point.boolValue)
    
    
    #print(point.properties.name, point.properties.type, point.properties.description, point.value)



#with open('points.txt','w', encoding='utf-8') as f:
    #i=0
    #while i<1:
        #obj_list = bacnet.read('192.168.1.155 device 518083 objectList')
        #f.write(datetime.now().strftime('%d.%m.%Y %H:%M'))
        #f.write(str(controller.points))
        #for point in controller.points:
            #print(type(point))
            #print(dir(point)) #все доступные параметры для объекта Python
        

