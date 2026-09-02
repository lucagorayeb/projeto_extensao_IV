import os
from dotenv import load_dotenv
from pathlib import Path
from manipulate_data_from_clean_files import list_files, count_files_itens

load_dotenv()

caminho = Path(__file__).parent.parent

disciplinas_limpas = f"{caminho}/{os.getenv("DISCIPLINAS_LIMPAS")}"

files = [disciplinas_limpas]

# list_files(files)
count_files_itens(files)
