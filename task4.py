import random

class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = random.randint(20, 120)
        self.color = color
        self.name = name
        self._is_police = is_polise

    def __bool__(self):
        return self._is_police == 'is_police'

    def show_speed(self):
        return self.speed

    def go(self):
        go ='Машина поехала'
        return go


    def stop(self):
        stop = 'Машина остановилась'
        return stop

    def turn_dirrection(self):
        dir = input('выберите в какую сторону повернуть (left, right): ')
        if dir == 'left':
            print('машина повернула влево')
        elif dir == 'right':
            print('машина повернула вправо')
        else:
            print('машина никуда не повернула')


class TownCar (Car):

    def show_speed(self):
        if self.speed < 60:
            print("скорость не превышена")
        else:
            print('вы превысили допусиммую скорость')
        return self.speed

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed < 40:
            print("скорость не превышена")
        else:
            print('вы превысили допусиммую скорость')
        return self.speed


class PoliceCar(Car):
    pass


# a = TownCar('speed', 'black', 'mazda', 1312)
# print(a.show_speed())
# print(a.name)
# print(a.__bool__())
# print(a.turn_dirrection(dir()))

b = WorkCar('speed', 'red', 'ferrari', 1312)
print(b.show_speed())
print(b.name)
print(b.__bool__())
print(b.stop())

c = PoliceCar('speed', 'grey', 'UAZ', 'is_police')
print(c.go())
print(c.show_speed())
print(c.name)
print(c.__bool__())
print(c.stop())
