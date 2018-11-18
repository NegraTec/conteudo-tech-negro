from unittest import TestCase, mock
from app.models import Conteudo, Autora
from app.service.conteudo_service import ConteudoService


class TestConteudoService(TestCase):

    @mock.patch('app.store.conteudo_store.ConteudoStore.listar_conteudos')
    @mock.patch('app.store.conteudo_store.ConteudoStore.obter_autora')
    def test_obter_conteudo_com_autora(self, obter_autora_mock, conteudo_store_mock):
        conteudo_store_mock.return_value = [
            Conteudo(
                titulo='algum titulo',
                url='alguma url',
                resumo='algum resumo',
                imagem='alguma imagem',
                autora_id=1)
        ]
        obter_autora_mock.return_value = Autora(nome='algum nome')

        conteudo_view = ConteudoService().listar_conteudos()

        self.assertEqual('algum titulo', conteudo_view[0]['titulo'])
        self.assertEqual('alguma url', conteudo_view[0]['url'])
        self.assertEqual('algum resumo', conteudo_view[0]['resumo'])
        self.assertEqual('alguma imagem', conteudo_view[0]['imagem'])
        self.assertEqual('algum nome', conteudo_view[0]['nome'])

    def test_obter_conteudo_destaque_com_autora(self):
        conteudos = [
            Conteudo(
                titulo='algum titulo',
                url='alguma url',
                resumo='algum resumo',
                imagem='alguma imagem',
                autora_id=1),
            Conteudo(
                titulo='algum titulo1',
                url='alguma url1',
                resumo='algum resumo1',
                imagem='alguma imagem1',
                autora_id=1
            )]
        conteudo_destaque = ConteudoService.obter_conteudo_destaque(conteudos)

        self.assertIn(conteudo_destaque, conteudos)