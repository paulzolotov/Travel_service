#! /usr/local/bin/python3

'''
Реализовать функцию, которая получает изменяемое количество словарей 
(ключи - буквы, значения - числа) и объединяет их в один словарь.
Значения dict должны быть суммированы в случае идентичных ключей
def combine_dicts(*args):
    ...

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2)
{'a': 300, 'b': 200, 'c': 300}

'''



def combine_dicts(*args):
    new_dict = {}
    for i_dict in args:
        for key, val in i_dict.items():
            if key not in new_dict:
                new_dict[key] = val
            else:
                new_dict[key] += val
    return new_dict

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2, dict_3))
