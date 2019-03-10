import os
from werkzeug.security import generate_password_hash
from app.store.user_store import UserStore


class UserService:

    @staticmethod
    def obter_usuaria_por_id(usuaria_id):
        return UserStore.obter_usuaria_por_id(usuaria_id)

    @staticmethod
    def obter_usuaria_por_login(usuaria_login):
        return UserStore.obter_usuaria_por_login(usuaria_login)

    @staticmethod
    def criar_usuaria_admin():
        login = os.getenv('ADMIN_LOGIN')
        senha = generate_password_hash(os.getenv('ADMIN_SENHA'))

        ja_existe_admin = UserStore.obter_usuaria_por_login(login)

        if not ja_existe_admin:
            print('Criando usuaria admin.')
            UserStore.criar(login, senha)