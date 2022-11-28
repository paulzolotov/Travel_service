"""
2. Создать 2 класса Truck и Sedan, которые являются наследниками Auto. Класс Truck имеет
дополнительный обязательный атрибут max_load. Переопределить метод drive, который перед
появлением сообщения «Car <brand> <mark> drives» выводит сообщение «Attention!».
Реализовать дополнительный метод load. При его вызове происходит пауза в 1 секунду
(используя модуль time), затем выводится сообщение «load», а затем снова происходит
пауза в 1 секунду. Класс Sedan имеет дополнительный метод обязательный атрибут max_speed
и при вызове метода drive, после появления сообщения «Car <brand> <mark> drives», выводит
сообщение «max speed of sedan <brand> <mark> is <max_speed>». Инициализировать по 2 отдельных
объекта этих классов, проверить работы их методов и атрибутов (вызвать методы, атрибуты вывести в печать)
"""

import time


class Auto:
    """ Auto description"""

    color = 'white'
    weight = 1.5e3  # Масса машины учитывается в кг

    def __init__(self, brand: str, mark: str, age: int):
        self.brand = brand
        self.mark = mark
        self.age = age

    def drive(self):
        print(f'Car {self.brand} {self.mark} drives.')

    def use(self):
        print(f'The car has been in use since {self.age+1}.')

    def stop(self):
        print(f'Car {self.brand} {self.mark} stops.')


class Truck(Auto):
    """ Truck description"""

    max_load = 20e3  # Масса загрузки прицепа учитывается в кг

    def drive(self):
        print('Attention!')
        super().drive()

    def load(self):
        time.sleep(1)
        print('load ...')
        time.sleep(1)


class Sedan(Auto):
    """ Sedan description"""

    max_speed = 180  # km/h

    def drive(self):
        super().drive()
        print(f'Max speed of sedan {self.brand} {self.mark} is {self.max_speed} km/h.', sep='\n')


car1 = Truck('МАЗ', '544008', 2010)
car1.load()
car1.drive()
car1.use()
car1.stop()
print(car1.max_load)

car2 = Sedan('Volkswagen', 'Polo sedan', 2018)
car2.drive()
car2.use()
car2.stop()
print(car2.max_speed)
