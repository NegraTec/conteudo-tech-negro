from app import app
from flask import render_template

from app.service.conteudo_service import ConteudoService


@app.route("/")
def index():
    conteudo_view = ConteudoService().listar_conteudos()

    destaque = ConteudoService.obter_conteudo_destaque(conteudo_view)

    return render_template('index.html', conteudos=conteudo_view, destaque=destaque)