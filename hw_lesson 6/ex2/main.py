#! /usr/local/bin/python3

def swap_el_str(s_str):
    new_l = []
    for i in s_str:
        if i == '"':
           new_l.append("'")
        elif i == "'":
           new_l.append('"')
        else:
            new_l.append(i)
    return ''.join(new_l)


user_str_1 = '"Python"is"Amazing"'
new_user_str_1 = swap_el_str(user_str_1)
print(f'{user_str_1} ---> {new_user_str_1}')
user_str_2 = "'Python'is'Amazing'"
new_user_str_2 = swap_el_str(user_str_2)
print(f'{user_str_2} ---> {new_user_str_2}')
