#! /usr/local/bin/python3

while 1:
    birth_str = input('Введите дату своего рождения в формате «день/месяц/год»: ')
    user_str = input('Введите дату в формате «день/месяц/год»: ')
    birth_l = birth_str.split('/')
    user_l = user_str.split('/')
    birthday = (365 * int(birth_l[2])) + (30 * int(birth_l[1])) + int(birth_l[0])
    user_day = (365 * int(user_l[2])) + (30 * int(user_l[1])) + int(user_l[0])
    if user_day >= birthday:
        years = (user_day - birthday) // 365
        days = (user_day - birthday) % 365
        print('Поздравляю! Вам:', years, '(год/года/лет)', days, '(день/дня/дней)')
    else:
        print('На момент введенной Вами даты Вы еще не родились!')

