class Config:
    PATH = "/usr/logs"
    INDENT = 4


class Development(Config):
    DEBUG_MODE = True
    DB_HOST = 'localhost:5432'
