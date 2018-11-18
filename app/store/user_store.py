from app.store.models import User


class UserStore:
    @staticmethod
    def obter_usuaria_por_id(usuaria_id):
        return User.query.get(usuaria_id)

    @staticmethod
    def obter_usuaria_por_login(usuaria_login):
        return User.query.filter_by(login=usuaria_login).first()
