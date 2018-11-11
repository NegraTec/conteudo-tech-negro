from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    conteudos = [
        {
            'nome': 'Roselma Mendes',
            'url': 'https://roselmamendes.github.io/tec/auditoria/',
            'titulo': 'Logging',
            'imagem': 'https://roselmamendes.github.io/images//logging/print-log.png',
            'resumo': ''}
    ]
    return render_template('index.html', conteudos=conteudos)