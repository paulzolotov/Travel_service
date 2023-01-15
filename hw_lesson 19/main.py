"""
Модифицируйте проект из ДЗ 18.
1) Модифицируйте эндпоинт /quote — при передаче дополнительным параметром запроса числа number выводится требуемое
количество цитат (при отсутствии параметра — выводится 1 цитата), например
GET {BASE_URL}/quote?number=3
«цитата 1»
«цитата 2»
«цитата 3»
GET {BASE_URL}/quote
«цитата 1»
2) Добавьте /register который должен принимать POST запрос от пользователя с формой с данными (login, email, password).
 С помощью валидатора из ДЗ13 (задание 3) проверьте корректность переданных данных и в случае корректности
 данных верните сообщение об успешности регистрации с кодом ответа 202 и статусом «Valid», в случае ошибок валидации —
 сообщение об ошибке, код ответа 406 и статус «Validation Error»
"""

from flask import Flask
from flask_app.app1.view import app1


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Development')
    app.register_blueprint(app1)
    return app


if __name__ == "__main__":
    create_app().run()
