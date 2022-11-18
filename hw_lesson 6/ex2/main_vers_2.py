#! /usr/local/bin/python3

'''
Создайте функцию которая получает в качестве аргумента 
произвольную строку и заменяет все символы " на ' и наоборот
'''


def swap_el_str(s_str):
    new_l = list(s_str)
    for i in range(len(new_l)):
        if new_l[i] == '"':
            new_l[i] = "'"
        elif new_l[i] == "'":
            new_l[i] = '"'
    return ''.join(new_l)


user_str_1 = '"Python"is"Amazing"'
new_user_str_1 = swap_el_str(user_str_1)
print(f'{user_str_1} ---> {new_user_str_1}')
user_str_2 = "'Python'is'Amazing'"
new_user_str_2 = swap_el_str(user_str_2)
print(f'{user_str_2} ---> {new_user_str_2}')
