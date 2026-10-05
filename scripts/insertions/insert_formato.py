from app.backend.modules.formato.formato_controller import (
    FormatoController
)
from dotenv import load_dotenv
import os

load_dotenv()


def insert_formatos():
    file = os.getenv("CLEAN_FORMATOS_FILE_WITHOUT_DUPLICATES")
    controller = FormatoController()
    with open(file, 'r', encoding="utf-8") as roteiro:
        formatos = roteiro.read().split('\n')
        for row in formatos:
            dados = {"nome": row}
            controller.insrt_formato_controller(dados)
