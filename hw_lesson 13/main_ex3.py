"""
Создайте класс Validator, который позволяет проводить проверку данных пользователя при
регистрации передаваемых в виде кортежа (login, password, email).
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — от 6 до 10 символов английского алфавит и цифр 0-9 в любой последовательности
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Проверку на соответствие правилам выполнить регулярными выражениями. По результатам работы метода validate пользователь
получит True если все 3 элемента прошли проверку, в противном случае - False
"""

import re
import Exceptions_ex3 as Exc


class Validator:

    def __init__(self, user_data: tuple) -> None:
        self.user_data = user_data if self.validate(user_data) else None

    def validate(self, user_data: tuple) -> None:
        try:
            self.validate_login(user_data[0])
            self.validate_password(user_data[1])
            self.validate_email(user_data[2])
            print('Валидация прошла успешна')
        except (Exc.InvalidLogin, Exc.InvalidPassword, Exc.InvalidEmail) as error:
            raise Exc.ValidationError('Валидация не пройдена') from error

    @staticmethod
    def validate_login(login) -> bool:
        if re.match(r'\b\w{6,10}\b', login):
            return True
        else:
            raise Exc.InvalidLogin(f'login {login} не прошел валидацию')

    @staticmethod
    def validate_password(password) -> bool:
        if re.match(r'[0-9a-zA-Z$%#^]{8,}$', password):
            return True
        else:
            raise Exc.InvalidPassword(f'password {password} не прошел валидацию')

    @staticmethod
    def validate_email(email) -> bool:
        if re.match(r'^[-\w\.]+@([-\w]+\.)+[-\w]{2}$', email):
            return True
        else:
            raise Exc.InvalidEmail(f'email {email} не прошел валидацию')


data = ('someuser12', 'passWORd%', 'mymail100@mymail.ru')
v = Validator(data)
