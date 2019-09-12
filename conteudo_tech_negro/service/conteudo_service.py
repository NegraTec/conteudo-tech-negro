import random
from conteudo_tech_negro.store.conteudo_store import ConteudoStore


class ConteudoService:

    def listar_conteudos(self):
        conteudos = ConteudoStore.listar_conteudos()

        conteudo_view = self._criar_conteudo_view(conteudos)

        return conteudo_view

    def _criar_conteudo_view(self, conteudos):
        conteudo_view = []
        for conteudo in conteudos:
            autora = ConteudoStore.obter_autora(conteudo.autora_id)
            conteudo_view.append(
                {
                    'titulo': conteudo.titulo,
                    'url': conteudo.url,
                    'resumo': conteudo.resumo,
                    'nome': autora.nome,
                    'imagem': conteudo.imagem if conteudo.imagem else ''
                }
            )

        return conteudo_view

    @staticmethod
    def obter_conteudo_destaque(conteudos):
        return random.choice(conteudos) if conteudos else None
