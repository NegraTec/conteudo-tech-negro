from flask import Flask, render_template
import random
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('URL_BANCO_DADOS')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Autora(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(250), nullable=False)
    redes_sociais = db.Column(db.String(250))

    def __init__(self, nome, redes_sociais):
        self.nome = nome
        self.redes_sociais = redes_sociais

    def __repr__(self):
        return '<Autora %r>' % self.nome


class Conteudo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(250))
    url = db.Column(db.String(250))
    resumo = db.Column(db.String(250), nullable=False)
    data_adicao = db.Column(db.Date)
    autora_id = db.Column(db.Integer, db.ForeignKey('autora.id'))
    autora = db.relationship('Autora')
    tema = db.Column(db.String(250))
    tipo_conteudo = db.Column(db.String(250))
    imagem = db.Column(db.String(250))

    def __init__(self, titulo, url, resumo, data_adicao, autora, tema, tipo_conteudo, imagem):
        self.tema = tema
        self.tipo_conteudo = tipo_conteudo
        self.imagem = imagem
        self.titulo = titulo
        self.url = url
        self.resumo = resumo
        self.data_adicao = data_adicao
        self.autora = autora

    def __repr__(self):
        return '<Conteudo %r>' % self.titulo


db.create_all()


def criar_conteudo_view(conteudos):
    conteudo_view = []
    for conteudo in conteudos:
        autora = Autora.query.filter_by(id=conteudo.autora_id).first()
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
    conteudos = Conteudo.query.all()

    conteudo_view = criar_conteudo_view(conteudos)

    destaque = random.choice(conteudo_view) if conteudos else None

    return render_template('index.html', conteudos=conteudo_view, destaque=destaque)