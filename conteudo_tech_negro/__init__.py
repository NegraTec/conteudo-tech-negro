import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'any random string'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('URL_BANCO_DADOS')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

from conteudo_tech_negro import routes
from conteudo_tech_negro.store import models
from conteudo_tech_negro import admin_configuracao

if not os.getenv('TESTES'):
    # flask migrate command to be used on GAE
    with app.app_context():
        upgrade()

    admin_configuracao.criar_usuaria_admin()
