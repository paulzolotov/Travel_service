#! /usr/local/bin/python3

while 1:
    height = float(input('Введите свой рост в м: '))
    weight = float(input('Введите свой вес в кг: '))
    print("Ваш индекс массы тела равен: ", weight / (height**2), '(кг/м2)')

