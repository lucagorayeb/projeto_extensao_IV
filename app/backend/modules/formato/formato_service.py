from .formato_repository import FormatoRepository
from ..base_json.retorno_json import RetornoJson

class FormatoService:

    def __init__(self):
        self.repo = FormatoRepository()
        self.json = RetornoJson()

    def slct_formato_service(self) -> list[dict] | None:
        data = self.repo.select()
        return self.__normalize_data(data)

    def insrt_formato_service(self, data: dict) -> None:
        self.repo.insert(data)

    def updt_formato_service(self, data: dict, id: int) -> None:
        data["id"] = id
        self.repo.update(data)

    def del_formato_service(self, id: int) -> None:
        data = {"id": id}
        self.repo.delete(data)

    def slct_by_id_formato_service(self, id: int) -> list[dict] | None:
        data = {"id": id}
        return self.__normalize_data(data)

    def __normalize_data(self, data: object) -> list[dict] | None:
        normalized_data = []
        for d in data:
            normalized_data.append({
                "id": d.id,
                "nome_formato": d.nome
            })
        return self.json.retorna_dados_formatados(normalized_data)
