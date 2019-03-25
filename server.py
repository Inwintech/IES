
import BAC0
import time

bacnet = BAC0.connect(ip='192.168.0.10')


controller = BAC0.device('192.168.0.90', 127001, bacnet)
points = controller.points

count_points = len(points)
print(count_points)

while True:
    for i in range(count_points):
        str_controller = str(points[i])
        print(str_controller)
        result_data = str_controller.rsplit(" ")
        print(result_data[2])
    time.sleep(5)
