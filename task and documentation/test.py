import BAC0
import time

bacnet = BAC0.connect(ip='192.168.0.10')


controller = BAC0.device('192.168.0.90', 127001, bacnet,poll=0)
while True:
    now_result = controller.points[1].properties
    result_read = controller.points[1].value
    print(now_result)
    print(result_read)
    time.sleep(5)

