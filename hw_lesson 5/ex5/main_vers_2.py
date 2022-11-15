#! /usr/local/bin/python3

while True:
    user_str = input().lower()
    user_dict = {}
    for item in set(user_str):
        user_dict[item] = user_str.count(item)
    print(user_dict)
