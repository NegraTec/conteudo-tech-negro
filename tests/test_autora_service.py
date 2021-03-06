from unittest import TestCase, mock
from conteudo_tech_negro.service.autora_service import AutoraService
from conteudo_tech_negro.store.models import Autora


class TestAutoraService(TestCase):

	@mock.patch('conteudo_tech_negro.store.autora_store.AutoraStore.cadastrar_autora')
	def test_cadastrar_autora(self, autora_store_cadastrar_autora):
		autora_store_cadastrar_autora.return_value = Autora(
			nome='Icaro',
			redes_sociais='linkedin: Icaro Henrique'
		)

		autora_json ={
			'nome': 'Icaro',
			'redes_sociais': 'linkedin: Icaro Henrique'
		}

		autora = AutoraService.cadastrar_autora(autora_json)

		autora_store_cadastrar_autora.assert_called_once_with(autora_json)

		self.assertEqual(autora.nome, 'Icaro')
		self.assertEqual(autora.redes_sociais, 'linkedin: Icaro Henrique')