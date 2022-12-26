"""
Создайте проект на основе фреймворка Flask. Реализуйте 2 эндпоинта:
1. /time — при обращении по данному пути клиенту возвращается текущее время в формате ISO 8601
2. /quote - при обращении по данному пути клиенту возвращается цитата Канье Уэста. Цитату можно получить
по адресу https://api.kanye.rest с применением библиотеки requests.
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
