#! /usr/local/bin/python3

'''
Реализовать функцию, которая будет работать аналогично функции map, 
без использования map (возвращаемым объектом может быть список)
'''


def my_map(func, *iterables) -> list:
    '''
    This function is similar built-in function 'map'.
    Make an iterator that computes the function using arguments from each of the iterables.
    Stops when the shortest iterable is exhausted.

    :param func: any function
    :param iterables: iterable object
    :return: list
    '''
    res = []
    shortest_iter = sorted([len(i) for i in iterables])[0]  # Узнаем самую короткую последовательность
    for i in range(shortest_iter):  # выбираем номер элемента из последовательности
        iterables_for_func = []
        for iter in iterables:  # создаем список из i-ых элементов последовательностей
             iterables_for_func.append(iter[i])
        res.append(func(*iterables_for_func))
    return res


# Сравнение работоспособности
seq1 = [1, 2, 3, 5, 6]
seq2 = [3, 4, 5]
seq3 = [1, 2]

a = my_map(lambda x, y, c: x+y+c, seq1, seq2, seq3)
print(a)
b = list(map(lambda x, y, c: x+y+c, seq1, seq2, seq3))
print(b)


