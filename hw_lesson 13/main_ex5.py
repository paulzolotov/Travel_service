"""
Реализуйте генератор, который будет бесконечно генерировать числа Фибоначчи.
(https://en.wikipedia.org/wiki/Fibonacci_number).
Пример:
>> gen = endless_fib_generator()
>> while True:
    print(next(gen))
>> 1 1 2 3 5 8 13 ...
"""


def endless_fib_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b


gen = endless_fib_generator()
while True:
    print(next(gen))  # тут лучше поставить breakpoint и отслеживать шаг за шагом
