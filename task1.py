import time
from itertools import cycle
class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        print('светофор запускается')
        color = ['red', 'yellow', 'green']
        while True:
            ww = cycle(color)
            print(next(ww))
            time.sleep(7)
            print(next(ww))
            time.sleep(2)
            print(next(ww))
            time.sleep(5)
        return ww

a = TrafficLight('a')
print(a.running())

