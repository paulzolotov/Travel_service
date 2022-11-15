#! /usr/local/bin/python3

def sum_func(s_l):
    n_l = list()
    s_l_int = [int(i) for i in list(s_l)]
    [n_l.append(sum(s_l_int) - i) for i in s_l]
    return n_l


some_list = [1, 2, 3, 4, 5]
new_list = sum_func(some_list)
print(new_list)
