#! /usr/local/bin/python3

while 1:
    ''' Скрипт работает как с целыми так и 
	с дробными числами'''
    s_str = input('Введите произвольное число: ')
    s = s_str.split(".")
    first_part = s[0]  # Целая часть числа
    if len(s) > 1:
        sec_part = s[1]  # Дробная часть числа
        full_s_str = s[0] + s[1]
    else:
        full_s_str = first_part
    sum_a = 0
    for number in full_s_str:
        sum_a += int(number)
    print("Сумма цифр данного числа равна: ", sum_a)

