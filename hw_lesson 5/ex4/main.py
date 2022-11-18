#! /usr/local/bin/python3

'''
Создайте программу которая генерирует случайное число в интервале от 1 до 100 
и предлагает пользователю угадать это число. В случает ввода от пользователя 
инструкции «stop», завершает работу и выводит загаданное число
для генерации случайного числа используйте метод randint модуля random

'''


import random

while True:
    print('Привет!Попробуй угадать мое число!\nВведи целое число от 1 до 100: ')
    rd_number = random.randint(1, 100)
    print(rd_number)
    count = 1
    while True:
        user_text = input().lower()
        if user_text == 'stop':
            print(f'Эх, спустя {count} попыт(ок/ки/ку) ты сдался.\nМое число было {rd_number}\n')
            break
        elif user_text.isalpha():
            print('Введи пожалуйста число!Или stop для прерывания игры')
        elif int(user_text) == rd_number:
            print(f'Невероятно!Ты угадал мое число (с/co) {count} попыт(ки/ок).\nПоздравляю!\n')
            break
        elif not 1 <= int(user_text) <= 100:
            print('Выбери число из промежутка!')
        count += 1
