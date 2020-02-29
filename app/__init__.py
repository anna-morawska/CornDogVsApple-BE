import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask 
from flask_restplus import Api, Resource, fields
from os import environ, getenv
import json

app = Flask(__name__)
api = Api(app)

environment = getenv('ENV', default='development')

if environment == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

environ["GOOGLE_APPLICATION_CREDENTIALS"] = app.config["GOOGLE_APPLICATION_CREDENTIALS"]
with open(app.config["GOOGLE_APPLICATION_CREDENTIALS"], "w") as file:
    file.write(getenv('GOOGLE_CONFIG'))

from app import routes
from app import my_utils
from app import classify_image