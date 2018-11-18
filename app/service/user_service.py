from app.store.user_store import UserStore


class UserService:

    @staticmethod
    def obter_usuaria_por_id(usuaria_id):
        return UserStore.obter_usuaria_por_id(usuaria_id)

    @staticmethod
    def obter_usuaria_por_login(usuaria_login):
        return UserStore.obter_usuaria_por_login(usuaria_login)