
import BAC0
import time

bacnet = BAC0.connect(ip='192.168.0.10')


controller = BAC0.device('192.168.0.90', 127001, bacnet,poll=0)
points = controller.points

count_points = len(points)
print(count_points)

while True:
    for i in range(count_points):
        value_controller = points[i].value
        print(value_controller)
    time.sleep(5)
