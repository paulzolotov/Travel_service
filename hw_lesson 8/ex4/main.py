#! /usr/local/bin/python3

'''
Имеется строка, содержащая имена через запятую «Tim,John,Sally,Trevor,Harry» и соответствующий
именам кортеж содержащий возраст (12,34,24,57,18).
Создать новый словарь, который будет иметь следующую структуру.
Ключ — сгенерированое шестизначное число, значения — словарь который состоит из 2 ключей «name» и «age»
с соответствующими значениями из строки с именами и кортежа с возрастами, например
{
	'127492': {
			'name': 'Tim',
			'age': 12
		},
	'538956': {
		…..
}
Сохранить итоговый словарь в виде json файла
'''

from random import randint
import json


def write_json(name_str: str, ages: tuple):
    result = dict()
    name_list = name_str.split(',')
    for i in range(len(name_list)):
        person = dict()
        person['name'] = name_list[i]
        person['age'] = ages[i]
        result[str(randint(100000, 999999))] = person
    with open('humans_data.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)


m_name_str = 'Tim,John,Sally,Trevor,Harry'
m_ages = (12, 34, 24, 57, 18)
write_json(m_name_str, m_ages)
