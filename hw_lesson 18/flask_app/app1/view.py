from flask import Blueprint
import requests
import datetime

app1 = Blueprint('something', __name__)


@app1.route('/index')
def index():
    return '<em align="centre"> Hello from Flask server</em>'


@app1.route('/time')
def time_iso8601():
    return 'Current time: ' + datetime.datetime.now().time().isoformat()


@app1.route('/quote')
def quote():
    return requests.get('https://api.kanye.rest').json()['quote'] + '<br>Ⓒ Kanye West'
