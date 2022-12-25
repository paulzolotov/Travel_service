from flask import Blueprint
import requests

app1 = Blueprint('something', __name__)


@app1.route('/index')
def index():
    return '<em>Hello from Flask server</em>'


@app1.route('/time')
def time():
    return f'aaa'


@app1.route('/quote')
def quote():
    return f'Kanye'
