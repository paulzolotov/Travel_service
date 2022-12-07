"""
Реализуйте класс итератора EvenRange, который принимает начало и конец интервала
в качестве аргументов инициализации и выдает только четные числа во время итерации.
Если пользователь попытается выполнить итерацию после того, как он выдал все возможные
числа следует вывести «Out of number!».
Примечание: вообще не используйте функцию range()
Пример:
>> er1 = EvenRange(7,11)
next(er1)
>> 8
next(er1)
>> 10
next(er1)
>> "Out of numbers!"
next(er1)
>> "Out of numbers!"
>> er2 = EvenRange(3, 14)
>> for number in er2:
    print(number)
>> 4 6 8 10 12 "Out of numbers!"
"""


class OutOfNumbers(Exception):
    """Исключение, генерирующееся в том случае, если
       пользователь попытается выполнить итерацию после того,
       как он выдал все возможные числа"""
    pass


class EvenRange:

    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop
        self.index = self.start - 2  # - 2 чтобы не потерять первый элемент
        if self.index % 2:  # Если первое число нечетное, сделаем четным
            self.index += 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 2
        if self.index <= self.stop:
            return self.index
        else:
            raise OutOfNumbers('Out of numbers!')


# er1 = EvenRange(8, 12)
# print(next(er1))
# print(next(er1))
# print(next(er1))
# print(next(er1))

er2 = EvenRange(3, 14)
for number in er2:
    print(number)
