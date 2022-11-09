#! /usr/local/bin/python3

while True:
    number = int(input('Введите число: '))
    if number > 0:
        for i in range(0, number+1):
            print(f'Число {i}, квадрат {i**2}')
    elif number < 0:
        for i in range(number, 0):
            print(f'Число {i}, квадрат {i**2}')
    else:
        print('Попробуйте еще раз!')
