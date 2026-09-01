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


def mostra_elementos_arquivos(table_name: str, array: list) -> None:
    for item in array:
        if table_name == 'formato_disciplina':
            insert_into_db_formato_disciplina(item)
        elif table_name == 'disciplinas':
            insert_into_db_disciplinas(item)
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


def insert_into_db_disciplinas(item: str) -> None:
    with engine.connect() as con:
        stmt = text("""INSERT INTO disciplinas
        (
            disciplina
        )
        VALUES
        (
            :item
        );""")
        con.execute(stmt, {'item': item})
        con.commit()


def select_formatos_from_bd(table_name: str) -> list[tuple]:
    with engine.connect() as con:
        stmt = text(f"SELECT * FROM {table_name};")
        return con.execute(stmt)


def mostra_dados_da_tabela(table_name: str) -> None:
    dados = select_formatos_from_bd(table_name)
    for id, item in dados:
        print(f"{id} - {item}")


# formatos_existentes = conta_elementos_arquivo(
#     'text_files/formato_disciplina_limpa.txt'
# )
# mostra_elementos_arquivos('formato_disciplina', formatos_existentes)
mostra_dados_da_tabela('formato_disciplina')

# disciplinas = conta_elementos_arquivo(
#     'text_files/disciplinas_limpas.txt'
# )
# mostra_elementos_arquivos('disciplinas', disciplinas)
mostra_dados_da_tabela('disciplinas')
