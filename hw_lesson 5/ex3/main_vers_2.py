#! /usr/local/bin/python3

while True:
    number = int(input('Введите число: '))
    negative = "" if number > 0 else "-"
    for i in range(1, abs(number) + 1):
        print(f"Число {negative}{i}, квадрат {i ** 2}")
