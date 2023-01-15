from flask import abort
import re
from . import Exceptions_register as Exc


class Validator:

    def __init__(self, user_data: dict) -> None:
        self.user_data = user_data if self.validate(user_data) else None

    def validate(self, user_data: dict):
        try:
            self.validate_login(user_data['login'])
            self.validate_password(user_data['password'])
            self.validate_email(user_data['email'])
        except (Exc.InvalidLogin, Exc.InvalidPassword, Exc.InvalidEmail) as error:
            raise Exc.ValidationError(f'{error}') from error
        except KeyError:
            abort(406, 'Enter 3 parameters: login, password, email.')

    @staticmethod
    def validate_login(login):
        if re.match(r'^\b\w{6,10}\b$', login):
            return True
        else:
            raise Exc.InvalidLogin(f'Login {login} failed validation.')

    @staticmethod
    def validate_password(password):
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            return True
        else:
            raise Exc.InvalidPassword(f'Password {password} failed validation.')

    @staticmethod
    def validate_email(email):
        if re.match(r'^[-\w\.]+@[-\w]+\.+[-\w]{2}$', email):
            return True
        else:
            raise Exc.InvalidEmail(f'Email {email} failed validation.')
