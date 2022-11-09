#! /usr/local/bin/python3

while True:
    user_str = input()
    user_dict = {}
    for i in  list(user_str.lower()):
        if i not in user_dict:
            user_dict[i] = 1
        else:
            user_dict[i] += 1
    print(user_dict)
