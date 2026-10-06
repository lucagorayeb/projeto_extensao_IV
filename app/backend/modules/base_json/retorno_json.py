import json


class RetornoJson:
    
    def retorna_dados_formatados(self, data: list[dict] | dict) -> str:
        return json.dumps(data, ensure_ascii=False, indent=4)