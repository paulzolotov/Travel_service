#! /usr/local/bin/python3

'''
Реализуйте функцию get_digits(num: int) -> tuple, которая возвращает кортеж
цифр заданного целого числа.
Пример:
get_digits(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
'''


def get_digits(num: int) -> tuple:
    a = [int(i) for i in str(num)]
    return tuple(a)

a_t = get_digits(87178291199)
print(a_t)
