#! /usr/local/bin/python3

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


