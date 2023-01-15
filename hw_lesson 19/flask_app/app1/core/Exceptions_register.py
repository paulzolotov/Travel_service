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
