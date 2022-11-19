#! /usr/local/bin/python3

'''
Откройте файл «unsorted_names.txt» содержащий имена студентов.
Прочитайте данные, отсортируйте их и запишите в новый файл «sorted_names.txt»
(каждое имя начинается с новой строки
_______
Aaron
Adrian
…..
Wiley
'''

with open('unsorted_names.txt', mode='r') as un_sort_file:
    sorted_names = sorted(un_sort_file.readlines())[1:]
with open('sorted_names.txt', mode='w') as sort_file:
    sort_file.write(''.join(sorted_names))

