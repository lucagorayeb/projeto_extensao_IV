import os
from dotenv import load_dotenv
from pathlib import Path
from manipulate_data_from_clean_files import list_files, count_files_itens
from clean_file_generator import (
    genetare_and_fused_clean_files,
    generate_clean_file,
    generate_clean_files_without_duplicates
)

load_dotenv()

duplicate_file = os.getenv("CLEAN_FORMATOS_FILE")
new_file = os.getenv("CLEAN_FORMATOS_FILE_WITHOUT_DUPLICATES")

generate_clean_files_without_duplicates(duplicate_file, new_file)