from flask import Blueprint, request, abort, Response, render_template, url_for
import requests
import datetime
import re
import flask_app.app1.Exceptions_register as Exc


app1 = Blueprint('something', __name__, template_folder='templates/app1')


class Validator:

    def __init__(self, user_data: dict) -> None:
        self.user_data = user_data if self.validate(user_data) else None

    def validate(self, user_data: dict):
        try:
            self.validate_login(user_data['login'])
            self.validate_password(user_data['password'])
            self.validate_email(user_data['email'])
        except (Exc.InvalidLogin, Exc.InvalidPassword, Exc.InvalidEmail) as error:
            abort(406, f'Validation error: {error}')
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


@app1.route('/home')
@app1.route('/index')
def index():
    return render_template('index.html')


@app1.route('/time')
def time_iso8601():
    return render_template('time.html', current_time='Current time: ' + datetime.datetime.now().time().isoformat())


@app1.route('/quote')
def quote():
    if request.args.get('number') is None:
        number = range(1)
    else:
        number = range(int(request.args.get('number')))
    return render_template('quote.html', req_list=[requests.get('https://api.kanye.rest').json().
                           get('quote') for _ in number])


@app1.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        abort(406, 'This page is for user registration. Submit a POST request.')
    elif request.method == 'POST':
        if Validator(request.form):
            return Response('Validation was successful', status=202)


@app1.route('/about')
def about():
    abort(404)


@app1.errorhandler(404)
def page_not_found(error):
    return 'This is not the web page you are looking for.'
