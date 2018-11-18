from unittest import TestCase, mock
from app.service.user_service import UserService
from app.store.models import User


class TestUserService(TestCase):

    @mock.patch('app.store.user_store.UserStore.obter_usuaria')
    def test_obter_usuario(self, obter_usuaria_mock):
        obter_usuaria_mock.return_value = User(login='algum login')
        usuaria_id = 1
        usuaria = UserService.obter_usuaria(usuaria_id)

        self.assertEqual('algum login', usuaria.login)