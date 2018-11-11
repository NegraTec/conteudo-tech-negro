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
            'resumo': 'Muita agua já rolou no meu papel de desenvolvedora, desde 2016 (quando postei pela primeira vez esse post). Agora um texto atualizado sobre a práticas de logs. E se você não loga na sua aplicação, eu aconselho a começar a fazer.',
            'tema': 'Monitoramento',
            'redes_sociais': 'twitter: roselmamendes',
            'data_adicao': '',
            'tipo_conteudo': 'texto'
        },
        {
            'nome': 'Will Mendes',
            'url': 'https://medium.com/@willmendesneto/publishing-angular-module-with-np-package-68d6c0650368',
            'titulo': 'Publishing Angular Module with NP package',
            'imagem': '',
            'resumo': '',
            'tema': 'Frontend',
            'redes_sociais': 'twitter: willmendesneto'
        },
        {
            'nome': 'Edla Santos',
            'url': 'https://medium.com/@edlasantos/quando-voc%C3%AA-assume-um-projeto-%C3%A9-pensado-em-v%C3%A1rias-coisas-b4351a13309a',
            'imagem': '',
            'resumo': '',
            'tema': 'Agilidade',
            'titulo': 'E a inception, como vai?',
            'redes_sociais': 'twitter: edladossantos1'
        },
        {
            'nome': 'Pedro Henrique',
            'url': 'https://medium.com/@pedrro/uma-breve-introdu%C3%A7%C3%A3o-a-teste-de-performance-31e788337157',
            'imagem': '',
            'resumo': '',
            'tema': 'Testes',
            'titulo': 'Uma breve introdução a teste de performance',
            'redes_sociais': 'twitter: pedrohns_'
        },
        {
            'nome': 'Dani Monteiro',
            'url': 'http://db4beginners.com/blog/postgresql-no-azure/',
            'titulo': 'Você conhece o PostgreSQL no Azure?',
            'imagem': 'http://db4beginners.com/wp-content/uploads/2018/11/ball-bright-close-up-207489-1-800x450.jpg',
            'resumo': '',
            'tema': 'Banco de Dados',
            'redes_sociais': 'twitter: DaniMonteiroDBA'
        }
    ]
    return render_template('index.html', conteudos=conteudos)