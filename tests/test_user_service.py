from unittest import TestCase, mock
from app.service.user_service import UserService
from app.store.models import User


class TestUserService(TestCase):

    @mock.patch('app.store.user_store.UserStore.obter_usuaria_por_id')
    def test_obter_usuaria_por_id(self, obter_usuaria_por_id_mock):
        obter_usuaria_por_id_mock.return_value = User(login='algum login')

        usuaria = UserService.obter_usuaria_por_id(1)

        self.assertEqual('algum login', usuaria.login)

    @mock.patch('app.store.user_store.UserStore.obter_usuaria_por_login')
    def test_obter_usuaria_por_login(self, obter_usuaria_por_login_mock):
        obter_usuaria_por_login_mock.return_value = User(login='algum login')

        usuaria = UserService.obter_usuaria_por_login('algum login')

        self.assertEqual('algum login', usuaria.login)