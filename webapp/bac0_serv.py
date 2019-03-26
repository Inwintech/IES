import BAC0
from datetime import datetime
import pandas as pd


bacnet = BAC0.connect(ip='192.168.1.104')
bacnet.whois()
bacnet.devices
controller = BAC0.device('192.168.1.155', 518083, bacnet)

print (bacnet.whois())
print (bacnet.devices)
print(controller)

for point in controller.points:
    if point.properties.type == 'analogInput' or point.properties.type == 'analogValue':
        print(point.value)
    else:
        print(point.boolValue)
    
    
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
        

