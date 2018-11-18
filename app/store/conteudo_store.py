from app.store.models import Conteudo, Autora


class ConteudoStore:

    @staticmethod
    def listar_conteudos():
        return Conteudo.query.all()

    @staticmethod
    def obter_autora(autora_id):
        return Autora.query.filter_by(id=autora_id).first()