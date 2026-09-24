from app.backend.modules.formatos.formatos_controller import (
    FormatoController as ctrlr
)
from dotenv import load_dotenv
import os

load_dotenv()

def insert_formatos():
    file = os.getenv("CLEAN_FORMATOS_FILE_WITHOUT_DUPLICATES")

    for i in file:
        print(i)
    # data = [
    #     "nome": ""
    # ]