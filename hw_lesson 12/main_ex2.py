'''
Создайте класс Validator, который позволяет проводить проверку данных пользователя при регистрации
передаваемых в виде кортежа (login, password, email).
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — не менее 6 символов
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Валидация каждого элемента в кортеже производится отдельным методом для каждого элемента (validate_email,
validate_login, validate_password) в которых в случае непрохождения валидации вызывается
ошибка (InvalidPassword, InvalidLogin, InvalidEmail), при соответствии — возвращается значение True.
В методе validate необходимо предусмотреть обработку этих ошибок и в случае их наличия — вызвать ошибку ValidationError.
Ошибки создать самостоятельно
например
validator = Validator()
validator.validate(user_login, Some!Password, mail@mail.com)
# True
validator.validate(user, Some!Password, mail@mail.com)
#  ValidationError
'''
import string


class ValidationError(Exception):
    """Исключение, генерирующееся в том случае, если
       один из 3ех параметров (login, password, email) не прошел валидацию"""
    pass


class InvalidLogin(Exception):
    """Исключение, генерирующееся в том случае, если
        login не прошел валидацию"""
    pass


class InvalidPassword(Exception):
    """Исключение, генерирующееся в том случае, если
        password не прошел валидацию"""
    pass


class InvalidEmail(Exception):
    """Исключение, генерирующееся в том случае, если
        email не прошел валидацию"""
    pass


class Validator:

    def __init__(self, user_data: tuple) -> None:
        self.user_data = user_data if self.validate(user_data) else None

    def validate(self, user_data: tuple) -> None:
        try:
            self.validate_login(user_data[0])
            self.validate_password(user_data[1])
            self.validate_email(user_data[2])
            print('Валидация прошла успешна')
        except (InvalidLogin, InvalidPassword, InvalidEmail):
            raise ValidationError('Валидация не пройдена')

    @staticmethod
    def validate_login(login) -> bool:
        if len(login) >= 6:
            return True
        else:
            raise InvalidLogin(f'login {login} не прошел валидацию')

    @staticmethod
    def validate_password(password) -> bool:
        if len(password) >= 8 \
                and any(char in string.ascii_lowercase for char in password) \
                and any(char in string.ascii_uppercase for char in password) \
                and any(char in '!"№;%:?*()-+@#$^&_=|/.,' for char in password):
            return True
        else:
            raise InvalidPassword(f'password {password} не прошел валидацию')

    @staticmethod
    def validate_email(email) -> bool:
        if any(char == '@' for char in email)\
                and email[-3] == '.' and all(char in string.ascii_lowercase for char in email[-1:-2]):
            return True
        else:
            raise InvalidEmail(f'email {email} не прошел валидацию')


data = ('user12', 'PASSWORd%', 'mymail@mail.co')
v = Validator(data)
