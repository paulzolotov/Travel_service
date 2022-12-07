"""
Создайте генераторную функцию которая в качестве аргумента принимать путь к файлу «unsorted_names.txt» и
букву английского алфавита, открывает файл по данному пути и генерирует
последовательность из имен начинающихся на указанную букву
>> names_with_letter = names_gen(«unsorted_names.txt», «A»)
>> next(names_with_letter)
Amelia
>> next(names_with_letter)
Adrienne
или
>> for name in names_with_letter:
        print(i, end=““)
Amelia
Adrienne
…
"""


def names_gen(file_path: str, letter: str):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(letter):
                yield line


names_with_letter = names_gen('unsorted_names.txt', 'V')
print(next(names_with_letter))
print(next(names_with_letter))

for name in names_with_letter:
    print(name, end='')
