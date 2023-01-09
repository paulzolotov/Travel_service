from flask import Blueprint, request, abort, Response, render_template, url_for
import requests
import datetime
from .core.validator import Validator


app1 = Blueprint('something', __name__, template_folder='templates/app1')


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
