import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from api.config import app_config

app = Flask(__name__)
CORS(app)
config_name = os.environ.get('APP_SETTINGS', 'development')
app.config.from_object(app_config.get(config_name))

db = SQLAlchemy(app) 

from api.blogs.blog import blog
app.register_blueprint(blog)
from api.blogs.auth import auth
app.register_blueprint(auth)
