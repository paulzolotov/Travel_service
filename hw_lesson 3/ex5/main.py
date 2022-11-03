#! /usr/local/bin/python3

while 1:
	first_str = input('Введите первое слово: ')
	sec_str = input('Введите второе слово: ')
	mod_first_str = first_str[1:-1]
	mod_sec_str = sec_str[1:-1]
	print('Итоговая строка: ', mod_first_str + mod_sec_str[::-1])
	

