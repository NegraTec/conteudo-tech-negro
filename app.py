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
            'resumo': 'Muita agua já rolou no meu papel de desenvolvedora, desde 2016 (quando postei pela primeira vez esse post). Agora um texto atualizado sobre a práticas de logs. E se você não loga na sua aplicação, eu aconselho a começar a fazer.'}
    ]
    return render_template('index.html', conteudos=conteudos)