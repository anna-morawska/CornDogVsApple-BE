import os

class Config(object):
    ENV="production"
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    IMAGE_UPLOADS = f'{os.getcwd()}/tmp/'
    GOOGLE_APPLICATION_CREDENTIALS = f'{os.getcwd()}/app/google-credentials-heroku.json'
    ALLOWED_IMAGE_EXTENSIONS = ["JPG", "JPEG", "PNG"]

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    ENV="development"
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False