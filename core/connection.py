import BAC0
import time



bacnet = BAC0.connect(ip='192.168.0.10')


controller = BAC0.device('192.168.0.90', 127001, bacnet)
points = controller.points

count_points = len(points)

while True:
    for i in range(count_points):
        find_value = ' '
        finish_str = points[i].rsplit(" ")
        print(finish_str)
    time.sleep(5)
