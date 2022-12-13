"""
Реализуйте свой пользовательский класс итератора с именем MySquareIterator, который дает
квадраты элементов коллекции, по которой он итерируется.
Пример:
>> lst = [1, 2, 3, 4, 5]
>> itr = MySquareIterator(lst)
>> for el in itr:
        print(el)
>> 1 4 9 16 25
"""
from typing import Any


class MySquareIterator:

    def __init__(self, obj: Any):
        self.obj = obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            i = self.obj[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return int(i)**2


# Реализовано для строк, списков, кортежей
# lst = [1, 2, 3, 4, 5]
# lst = (1, 2, 3, 4, 5)
lst = '12345'
itr = MySquareIterator(lst)
for el in itr:
    print(el, end=' ')
