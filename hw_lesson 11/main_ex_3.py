"""
Реализуйте класс DataObject, который имеет обязательный атрибут data (произвольного типа данных).
Реализуйте класс очередь (Deque) с атрибутом класса deque, в котором будут храниться элементы добавляемые в очередь.
Класс Deque имеет методы
- append_left для добавления элемента в начало очереди deque
- append_right для добавления элемента в конец очереди deque
(в данных методах необходимо реализовать возможность добавления в очередь только экземпляров класса DataObject
(и его дочерних), а также проверку длины очереди — одновременно там может находиться не более 5 элементов —
в случае добавления 6 элемента добавление не производится и пользователю выдается сообщение о переполнении очереди).
- pop_left — удаляет из очереди первый элемент слева и возвращает его
- pop_right - удаляет из очереди первый элемент справа и возвращает его
При реализации методов класса Deque воспользуйтесь методами класса (classmethod)
"""

from dataclasses import dataclass


@dataclass
class DataObject:
    data: object = None  # Можно еще так - data: Any = None (from typing import Any)


class Deque:

    deque = []

    @classmethod
    def append_left(cls, item: DataObject) -> None:
        if isinstance(item, DataObject):
            if len(cls.deque) < 5:
                cls.deque.insert(0, item)
            else:
                raise NotImplementedError('The deque is overflowing!')

    @classmethod
    def append_right(cls, item: DataObject) -> None:
        if isinstance(item, DataObject):
            if len(cls.deque) < 5:
                cls.deque.append(item)
            else:
                raise NotImplementedError('The deque is overflowing!')

    @classmethod
    def pop_left(cls) -> list:
        return cls.deque.pop(0)

    @classmethod
    def pop_right(cls) -> list:
        return cls.deque.pop(-1)


class Test:
    """Тестовый класс для проверки isinstance"""
    pass


# Создание экземпляров класса DataObject и заполнение атрибута data произвольными данными
a = DataObject()
a.data = [1, 3, 5]
b = DataObject()
b.data = 'hello'
c = DataObject()
c.data = 4

# Создание тестовых атрибутов
d = Test()

# Создание экземпляра класса Deque
my_deque = Deque()

# Проверка работоспособности функций на добавление элементов
my_deque.append_left(b)
my_deque.append_right(a)
my_deque.append_left(c)
my_deque.append_right(a)
my_deque.append_right(b)
my_deque.append_right(c)  # не добавится в очередь т.к элементов в очереди 5
# Проверка isinstance
my_deque.append_right(d)

# Отрисовка получившейся очереди
print(my_deque.deque)

# Проверка работоспособности функций на удаление элементов
print(my_deque.pop_right())
print(my_deque.pop_left())
