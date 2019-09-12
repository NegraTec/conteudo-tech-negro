from conteudo_tech_negro.store.autora_store import AutoraStore


class AutoraService:
	@staticmethod
	def cadastrar_autora(autora_json):
		return AutoraStore.cadastrar_autora(autora_json)
