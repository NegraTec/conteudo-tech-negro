from conteudo_tech_negro.store.models import User, db


class UserStore:
    @staticmethod
    def obter_usuaria_por_id(usuaria_id):
        return User.query.get(usuaria_id)

    @staticmethod
    def obter_usuaria_por_login(usuaria_login):
        return User.query.filter_by(login=usuaria_login).first()

    @staticmethod
    def criar(login, senha):
        usuaria = User()

        usuaria.id = 9999
        usuaria.login = login
        usuaria.password = senha

        db.session.add(usuaria)
        db.session.commit()
