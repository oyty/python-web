import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True


class ProductConfig(Config):
    pass


config = {
    'dev': DevConfig,
    'product': ProductConfig,
    'default': DevConfig
}
