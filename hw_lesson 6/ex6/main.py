#! /usr/local/bin/python3

'''
Создайте функцию которая работает так же как str.split() метод (естественно, без использования str.split())
'''


def my_str_split(u_str: str, sep=' ', maxsplit=-1) -> list:
    '''
     sep=' ' : Строка-разделитель, при помощи которой требуется разбить исходную строку. Может содержать как один,
     так и несколько символов. Если не указан, то разделителем считается пробельный символ.
     maxsplit =- 1 : Максимальное количество разбиений, которое требуется выполнить.
     Если -1, то количество разбиений не ограничено.
    '''
    n_l = []  # Результирующий список
    if isinstance(u_str, str):  # Проверка типа проверяемого аргумента
        o_str = ''  # символы строки до разделителя
        count = 0  # Счетчик разбиений
        if maxsplit == 0 or maxsplit < -2:  # Не разобрался как работает метод split при отрицательном
                                            # количестве разбиений. Я думал что количество должно быть положетельным.
            print('Argument "maxsplit" must be type positive or -1')
        for i in range(len(u_str)):
            if u_str[i] != sep:  # Сравнение элемента строки с разделителем
                o_str += u_str[i]
                if i == len(u_str)-1:  # Добавление последних символов строки, при условии,
                                        # что послений элемент не разделитель
                    n_l.append(o_str)
            else:
                n_l.append(o_str)
                o_str = ''
                count += 1
                if count == maxsplit:  # Заканчиваем итерации на нужном разделителе
                    n_l.append(u_str[i+1:len(u_str)])
                    return n_l
    else:
        print('Argument "u_str" must be type "string"')
    return n_l


a = 'a bce wgw'
c = 'a"bce"wgw'
b = []
print('Результат встроенного метода str.spit(): ', c.split(' ', maxsplit=1))
print('Результат дублирующей функции            ', my_str_split(c, sep=' ', maxsplit=1))
