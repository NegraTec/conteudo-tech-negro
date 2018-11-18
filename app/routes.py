from app import app
from flask import render_template
import random
from app.models import Conteudo, Autora


def criar_conteudo_view(conteudos):
    conteudo_view = []
    for conteudo in conteudos:
        autora = Autora.query.filter_by(id=conteudo.autora_id).first()
        conteudo_view.append(
            {
                'titulo': conteudo.titulo,
                'url': conteudo.url,
                'resumo': conteudo.resumo,
                'nome': autora.nome,
                'imagem': conteudo.imagem if conteudo.imagem else ''
            }
        )

    return conteudo_view


@app.route("/")
def index():
    conteudos = Conteudo.query.all()

    conteudo_view = criar_conteudo_view(conteudos)

    destaque = random.choice(conteudo_view) if conteudos else None

    return render_template('index.html', conteudos=conteudo_view, destaque=destaque)