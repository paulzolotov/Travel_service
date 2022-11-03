#! /usr/local/bin/python3

while 1:
	x = float(input('Введите число x: '))
	y = float(input('Введите число y: '))
	print("Результат выражения: ", (abs(x) - abs(y)) / (1 + abs(x * y)) )

