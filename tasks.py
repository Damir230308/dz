# task 1

import time
from itertools import cycle

class Trafficlight:
    def __init__(self):
        self.__color = (('red', 8), ('yellow', 2), ('green', 10))
    def running(self):
        for color, sec in cycle(self.__color):
            print(color, 'wait {} sec'.format(sec))
            time.sleep(sec)
traffic_light = Trafficlight()
traffic_light.running()

# task 2

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def mass_road(self):
        mass_road = self._lenght + self._width * 25 * 5 / 1000
        return mass_road
calc = Road(20, 20)
print(calc.mass_road(), 'C')

# task 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} пишет')
class Pen(Stationery):
    pass
class Pencil(Stationery):
    pass
class Handle(Stationery):
    pass

pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()

# task 4

class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color= color
        self.is_police = is_police
    def go(self):
        print('Машина поехала...')
    def stop(self):
        print('Машина остановилась...')
    def turn(self, direction):
        print(f'Машина повернула на {direction}')
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
class Towncar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Ваша скорость превышена! Вам штраф!')
class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Ваша скорость превышена! Вам штраф!')

class PoliceCar(Car):
    pass

town_car = Towncar('Mazda cx9', 100, 'green', is_police=False)
town_car.show_speed()
work_car = WorkCar('Mazda cx7', 60, 'blue', is_police=True)
work_car.show_speed()
work_car.go()
work_car.turn('налево')
work_car.stop()

# task 3

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']
class Position(Worker):
    def full_name(self):
        full_name = f'{self.name}, {self.surname}, {self.position}'
        return full_name
    def total_income(self):
        total_income = self._income_wage + self._income_bonus
        return total_income
position_full_name = Position('Damir', 'Oldov', 'mafia', {'wage': 1000000, 'bonus': 10000})
print(position_full_name.full_name())
print(position_full_name.total_income())
