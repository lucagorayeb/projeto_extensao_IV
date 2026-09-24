from .formatos_repository import (
    FormatoRepository as repo
)


class FormatoService:

    def slct_formato_service(self) -> list[tuple]:
        return repo.select()

    
    def insrt_formato_service(self, data: list[tuple]):
        repo.insert(data)

    
    def updt_formato_service(self, data: list[tuple], id: int):
        repo.update(data, id)

    
    def del_formato_service(self, id: int):
        repo.delete(id)
