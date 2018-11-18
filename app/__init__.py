import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'any random string'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('URL_BANCO_DADOS')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

from app import routes
from app import models
from app import admin_configuracao
