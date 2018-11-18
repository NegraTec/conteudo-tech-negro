from app.store.user_store import UserStore


class UserService:

    @staticmethod
    def obter_usuaria(usuaria_id):
        return UserStore.obter_usuaria(usuaria_id)