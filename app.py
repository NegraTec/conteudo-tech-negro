from flask import Flask, render_template
import random
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from admin_configuracao import configurar_admin
from banco_configuracao import configurar_banco

app = Flask(__name__)
app.secret_key = 'any random string'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('URL_BANCO_DADOS')
db = SQLAlchemy(app)

tabela_autora, tabela_conteudo, tabela_user = configurar_banco(db)
migrate = Migrate(app, db)

configurar_admin(app, db, {'tabela_autora': tabela_autora, 'tabela_conteudo': tabela_conteudo, 'tabela_user': tabela_user})


def criar_conteudo_view(conteudos):
    conteudo_view = []
    for conteudo in conteudos:
        autora = tabela_autora.query.filter_by(id=conteudo.autora_id).first()
        conteudo_view.append(
            {
                'titulo': conteudo.titulo,
                'url': conteudo.url,
                'resumo': conteudo.resumo,
                'nome': autora.nome
            }
        )

    return conteudo_view


@app.route("/")
def index():
    conteudos = tabela_conteudo.query.all()

    conteudo_view = criar_conteudo_view(conteudos)

    destaque = random.choice(conteudo_view) if conteudos else None

    return render_template('index.html', conteudos=conteudo_view, destaque=destaque)