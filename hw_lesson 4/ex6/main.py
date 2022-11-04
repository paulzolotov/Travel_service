#! /usr/local/bin/python3

while 1:
    s_str = input('Введите строку как минимум с 2-мя пробелами: ')
    s = s_str.lower().split()
    first_word = s[0].title()
    other_word = ' '.join(s[1:-1])
    last_word = s[-1].title()
    print('Ваша модифицированная строка:', ' '.join([first_word, other_word, last_word]))

