from .formato_repository import FormatoRepository
from ..base_json.retorno_json import RetornoJson

class FormatoService:

    def __init__(self):
        self.repo = FormatoRepository()
        self.retorna_json = RetornoJson()

    def slct_formato_service(self) -> list[dict] | None:
        dados = self.repo.select().fetchall()
        return self.__normaliza_dados(dados)

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
        return self.repo.select_by_id(data=data)

    def __normaliza_dados(self, data: object) -> list[dict] | None:
        dados_normalizados = []
        for cont in range(len(data)):
            for i in range(len(data[cont]) - 1):
                dados_normalizados.append({
                    "id": data[cont][i], 
                    "nome": data[cont][i+1]
                })
        return self.retorna_json.retorna_dados_formatados(dados_normalizados)
        # return dados_normalizados
        # print(json.dumps(dados_normalizados, ensure_ascii=False, indent=4))
