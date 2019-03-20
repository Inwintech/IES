import BAC0




bacnet = BAC0.connect(ip='192.168.1.105')
bacnet.whois()
bacnet.devices
controller = BAC0.device('192.168.1.155', 518083, bacnet)
obj_list = bacnet.read('192.168.1.155 device 518083 objectList')

print(controller)
print(obj_list)
print(controller.points[0])
print(controller.points[0].history)
