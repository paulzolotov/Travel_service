#! /usr/local/bin/python3

'''
Открыть файл из п.4. Создать функцию ('transform_to_csv') которая будет выполнять следующее:
каждую запись в json файле функция будет преобразовывать в строку с данными в виде name,age,id
(например, Tim,12,127492) и сохранять все данные в виде csv файла
Путь к json файлу и имя сохраняемого csv файла должно запрашиваться у пользователя

humans_data.json - примерный путь до json файла
humans_inf.csv - примерный название csv файла
'''

import json
import csv


def transform_to_csv(path_json: str, name_csv: str):
    with open(path_json, 'r') as json_file:
        data_p = json.load(json_file)
    # Стандартный спопосб
    fieldnames = ['name', 'age', 'id']
    with open(name_csv, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(fieldnames)
        for key, item in data_p.items():
            person = [item['name'], str(item['age']), key]
            csv_writer.writerow(person)
    # Способ с DictWriter
    # fieldnames = ['name', 'age', 'id']
    # with open(name_csv, 'w') as csv_file:
    #     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     csv_writer.writeheader()
    #     for key, item in data_p.items():
    #         person = [item['name'], str(item['age']), key]
    #         person_dict = dict(zip(fieldnames, person))
    #         csv_writer.writerow(person_dict)


user_path_json = input('Введите абсолютный путь до json файла: ')
user_name_csv = input('Введите имя сохраняемого csv файла: ')
transform_to_csv(user_path_json, user_name_csv)
