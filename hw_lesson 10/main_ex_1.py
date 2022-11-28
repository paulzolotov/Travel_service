"""
1. Создать родительский класс Auto, у которого есть атрибуты: brand, age, color, mark и weight.
В классе должны быть реализованы следующие методы — drive, use и stop. Методы drive и stop выводят
сообщение «Car <brand> <mark> drives / stops». Метод use увеличивает атрибут age на 1 год.
Атрибуты brand, age и mark необходимо инициализировать при объявлении объекта
"""


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


car1 = Auto('BMW', 'M8', 2020)
car1.drive()
car1.use()
car1.stop()

car2 = Auto('Mercedes-Benz ', 'AMG GT 63 S', 2019)
car2.drive()
car2.use()
car2.stop()
