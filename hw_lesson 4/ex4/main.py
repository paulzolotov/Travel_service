#! /usr/local/bin/python3

while 1:
    str1 = input('Введите первое слово: ')
    str2 = input('Введите второе слово: ')
    str3 = input('Введите третье слово: ')
    print('1. Буквы которые встречаются во всех словах: ', set(str1) & set(str2) & set(str3))
    print('2. Все буквы, которые хотя бы раз встречаются в слове: ', set(str1) | set(str2) | set(str3))
    print('3. Буквы в каждом слове которые не встречаются в других словах: ', (set(str1) - set(str2) - set(str3)) | (set(str2) - set(str1) - set(str3)) | (set(str3) - set(str1) - set(str2)))

