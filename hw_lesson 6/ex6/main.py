#! /usr/local/bin/python3

'''
Создайте функцию которая работает так же как str.split() метод (естественно, без использования str.split())
'''


def my_str_split(u_str: str, sep=' ', maxsplit: int = -1) -> list:
    '''
     sep=' ' : Строка-разделитель, при помощи которой требуется разбить исходную строку. Может содержать как один,
     так и несколько символов. Если не указан, то разделителем считается пробельный символ.
     maxsplit =- 1 : Максимальное количество разбиений, которое требуется выполнить.
     Если -1, то количество разбиений не ограничено.
    '''
    result = []  # Результирующий список
    if isinstance(u_str, str):  # Проверка типа проверяемого аргумента
        pos = 0
        for i in range(len(u_str)):
            if u_str[i] == sep[0]:  # Сравнение элемента строки с первым элементом разделителя
                sep_start = u_str.find(sep, pos)  # Находит индекс разделителя, если его нет то возвращает -1
                if sep_start != -1 and maxsplit != 0:  # Если разделитель есть и количество разбиений не равно 0
                    result.append(u_str[pos:sep_start])
                    pos = sep_start + len(sep)
                    maxsplit -= 1
        result.append(u_str[pos:])
    else:
        print('Argument "u_str" must be type "string"')
    return result
