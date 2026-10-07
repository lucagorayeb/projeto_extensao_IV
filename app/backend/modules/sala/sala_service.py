from .sala_repository import SalaRepository
from ..base_json.retorno_json import RetornoJson


class SalaService:

    def __init__(self):
        self.serv = SalaRepository()
        self.json = RetornoJson()

    def insrt_sala_service(self, data: dict) -> None:
        self.serv.select(data=data)

    def updt_sala_service(self, data: dict, id: int) -> None:
        data['id'] = id
        self.serv.update(data=data)

    def del_sala_service(self, id: int) -> None:
        data = {'id': id}
        self.serv.delete(data=data)

    def slct_sala_service(self) -> list[dict]:
        data = self.serv.select()
        return self.__normalize_data(data)

    def slct_by_id_sala_service(self, id: int) -> list[dict]:
        data = {'id': id}
        data = self.serv.select_by_id(data=data)
        return self.__normalize_data(data)

    def __normalize_data(self, data: object) -> str | None:
        normalized_data = []

        for d in data:
            normalized_data.append({
                "id": d.id,
                "nome_sala": d.nome_sala,
                "quantidade_alunos": d.limite_alunos,
                "tipo_sala": d.tipo_sala
            })
        return self.json.retorna_dados_formatados(normalized_data)