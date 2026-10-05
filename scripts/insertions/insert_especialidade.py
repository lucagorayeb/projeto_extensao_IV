from app.backend.modules.especialidade.especialidade_controller import (
    EspecialidadeController
)
import os
from dotenv import load_dotenv

load_dotenv()

file = os.getenv("ESPECIALIDADES_FILE")


def insrt_especialidade():
    contr = EspecialidadeController()
    with open(file, "r") as conteudo:
        f = conteudo.read().split('\n')
        for linha in f:
            data = {"nome": linha}
            contr.insrt_especialidade_controller(data)
