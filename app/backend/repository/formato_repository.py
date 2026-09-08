# from sqlalchemy import text
from .base_repository import BaseRepository as BR


class FormatoRepository(BR):

    def insert(item: str) -> None:
        # stmt = text("""INSERT INTO formato_disciplina
        # (
        #     formato_disciplina
        # )
        # VALUES
        # (
        #     :item
        # );""")
        print("Chegou até a função insert da tabela formato.")

    def select() -> list[tuple]:
        # stmt = text("SELECT id, formato_disciplina FROM formato_disciplina;")
        print("Chegou até a função select da tabela formato.")

    def update() -> None:
        print("Chegou até a função update da tabela formato.")

    def delete() -> None:
        print("Chegou até a função delete da tabela formato.")
