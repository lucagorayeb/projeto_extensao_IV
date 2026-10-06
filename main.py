# from app.backend.modules.disciplinas.disciplinas_controller import (
#     DisciplinasController as dc
# )
from app.backend.modules.formato.formato_controller import FormatoController
# from tests.db_connection_test import teste_conexao_bd
# from scripts.insertions.insert_formato import insert_formatos
# from scripts.insertions.insert_especialidade import insrt_especialidade
# from scripts.insertions.insert_tipo_sala import insert_tipo_sala

# try:
fc = FormatoController()
dados = fc.slct_formato_controller()
print(dados)
# except Exception as e:
#     print(f"Erro: {e}")

# try:
#     data = {"nome": "TESTE"}
#     fc.insrt_formatos_controller(data)
# except Exception as e:
#     print(f"Erro: {e}")

# teste_conexao_bd()
# insert_formatos()
# insrt_especialidade()
# insert_tipo_sala()