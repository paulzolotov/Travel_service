#! /usr/local/bin/python3

'''
Создайте декоратор log_function, который будет выполнять вывод в консоль информации о декорированной функии, в частности — время вызова, имя функции, информацию о типах аргументов, которые ожидаются для передачи в функцию, переданные аргументы (переданные по позиции и по ключевому слову), например

@ log_function
def test(a:int, b:str):
       print(a, b)

>>> test(1, 'time')

Вывод: 2022-11-16 08:44:42.290025 | Function: test | Expected: {'a': <class 'int'>, 'b': <class 'str'>} | Input: (1, 'time')
'''


import datetime


def log_function(function):
    def wrapper(*args, **kwargs):
        time_now = datetime.datetime.now()
        result = function(*args, **kwargs)
        print(f'{time_now} | Function: {function.__name__} | Expected: {function.__annotations__} | Input: {args}'
              f' {kwargs}')
        return result
    return wrapper


@log_function
def test(a: int, b: str):
    print(a, b)


test(1, 'time')
test(1, b='time')
test(a=1, b='time')


