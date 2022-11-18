#! /usr/local/bin/python3

'''
Напишите программу для подсчета количества символов (частоты символов) в строке (игнорируя регистр букв).
Пример:
Input: 'Oh, it is Python' 
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
'''


while True:
    user_str = input().lower()
    user_dict = {}
    for item in set(user_str):
        user_dict[item] = user_str.count(item)
    print(user_dict)
