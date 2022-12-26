class Config:
    PATH = "/usr/logs"
    INDENT = 4


class Development(Config):
    DEBUG = True
    SERVER_NAME = '127.0.0.1:5432'
