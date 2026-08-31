from sqlalchemy import text
from interface import engine


def conta_elementos_arquivo(file_txt: str) -> list:
    array = []
    with open(file_txt, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip('\n')
            if line not in array:
                array.append(line)
    return array


def mostra_elementos_arquivos(array: list) -> None:
    for item in array:
        insert_into_db_formato_disciplina(item)
        print(item)
    print('Já adicionados ao banco de dados')


def insert_into_db_formato_disciplina(item: str) -> None:
    with engine.connect() as con:
        stmt = text("""INSERT INTO formato_disciplina
        (
            formato_disciplina
        )
        VALUES
        (
            :item
        );""")
        con.execute(stmt, {'item': item})
        con.commit()


formatos_existentes = conta_elementos_arquivo(
    'text_files/formato_disciplina_limpa.txt'
)
mostra_elementos_arquivos(formatos_existentes)
