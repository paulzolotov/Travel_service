#! /usr/local/bin/python3

while 1:
    s_str = input('Введите последовательность слов через запятую: ')
    s = s_str.split(",")
    print('Список уникальных слов в отсортированном виде: ', ','.join(sorted(set(s))))

