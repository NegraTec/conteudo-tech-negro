from app.store.models import User


class UserStore:
    @staticmethod
    def obter_usuaria(usuaria_id):
        return User.query.get(usuaria_id)