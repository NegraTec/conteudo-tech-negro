from app import db


class Autora(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(250), nullable=False)
    redes_sociais = db.Column(db.String(250))

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

    def __repr__(self):
        return '<Conteudo %r>' % self.titulo


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(150))

    # Flask-Login integration
    # NOTE: is_authenticated, is_active, and is_anonymous
    # are methods in Flask-Login < 0.3.0
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username
