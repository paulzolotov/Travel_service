"""
Создайте класс, который имеет атрибут queue (допускается использование списка), который имеет метод add, позволяющий
добавлять в queue следующие объекты — целые числа, числа с плавающей запятой, строки.
При этом в момент добавления происходит валидация элементов по следующим правилам:
1. Целые числа — должны делится на 8, состоять из не более чем 4 символов
2. Числа с запятой — не более 3 символов после запятой
3. Строки — длина не более 4 символов без дублирования символов
В результате работы метода add элементы прошедшие валидацию добавляются в queuе.
Элементы, не прошедшие валидацию, выводятся пользователю с сообщением о причине не добавления, например:
q=Queue()
q.add(1, 16, 280, 80000, 2.51, 1.875, text, data, world, some)
InvalidIntDivision → 1 # не делится на 8
InvalidIntNumberCount → 80000 # больше 4 символов
InvalidFloat → 1.875 # больше 2 символов после запятой
InvalidTextLength → world # больше 4 символов
DuplicatesInText → data # повторяющиеся символы
q.queue
# [16,280,some]
"""


import Exceptions_ex3 as Exc


class Queue:
    queue: list = list()

    def add(self, *args) -> None:
        for i in args:
            try:
                if isinstance(i, int):
                    self.validate_int(i)
                if isinstance(i, float):
                    self.validate_float(i)
                if isinstance(i, str):
                    self.validate_str(i)
            except (Exc.InvalidIntDivision, Exc.InvalidIntNumberCount, Exc.InvalidFloat, Exc.InvalidTextLength,
                    Exc.DuplicatesInText) as ex:
                print(ex)
            except Exception as unk_ex:
                print(unk_ex)

    def validate_int(self, i: int) -> None:
        if len([int(j) for j in str(i)]) > 4:
            raise Exc.InvalidIntNumberCount(f'Число {i} состоит из более 4 цифр')
        elif i % 8:
            raise Exc.InvalidIntDivision(f'Число {i} не делится на 8 без остатка')
        else:
            self.queue.append(i)

    def validate_float(self, i: float) -> None:
        ind = str(i).find('.')
        if len(str(i)[ind:]) > 2:
            raise Exc.InvalidFloat(f'Число {i} имеет более 2ух символов после запятой')
        else:
            self.queue.append(i)

    def validate_str(self, i: str) -> None:
        if len(i) > 4:
            raise Exc.InvalidTextLength(f'Строка {i} состоит из более 4ех символов')
        elif len(set(i)) != len(i):
            raise Exc.DuplicatesInText(f'Строка {i} имеет дублирующие символы')
        else:
            self.queue.append(i)


q = Queue()
q.add(1, 16, 280, 80000, 2.51, 1.875, 'text', 'data', 'world', 'some')
print(q.queue)
