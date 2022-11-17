#! /usr/local/bin/python3

'''
    Для себя и читаемости lambda функции:

    b = tuple(filter(fun1, a)) - используем полученные ответ с fun1 и фильтруем относительно каждого слова в списке.
                                    Выводим результат в виде кортежа
    fun1 = lambda y: y[::1] == y[::-1] - проверяем слово на условие
'''


a = ["rotator", "abcd", "noon", "python", "lol", "ololo", "notnot"]

b = tuple(filter(lambda y: y[::1] == y[::-1], a))

print(b)

