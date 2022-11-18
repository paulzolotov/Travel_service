#! /usr/local/bin/python3

'''
Реализуйте функцию, которая получает список из целых чисел, и возвращает новый список, в котором каждый элемент с индексом i нового списка является суммой всех чисел в исходном списке, кроме числа i.

foo([1, 2, 3, 4, 5])
[14, 13, 12, 11, 10]

foo([3, 2, 1])
[3, 4, 5]
'''


def sum_func(s_l):
    '''Наверное можно решить проще, подумаю еще над другим способом'''
    n_l = list()
    for i in range(0, len(s_l)):
        addition_l = s_l.copy()
        _ = addition_l.pop(i)
        n_l.append(sum(addition_l))
    return n_l


some_list = [1, 2, 3, 4, 5]
new_list = sum_func(some_list)
print(new_list)
