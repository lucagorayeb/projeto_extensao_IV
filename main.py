# from app.backend.modules.disciplinas.disciplinas_controller import (
#     DisciplinasController as dc
# )
# from app.backend.modules.formatos.formatos_controller import (
#     FormatosController as fc
# )
# from scripts.insertions.insert_formatos import (
#     insert_formatos
# )
# from scripts.insertions.insert_especialidade import insrt_especialidade
# from tests.db_connection_test import teste_conexao_bd
from scripts.insertions.insert_tipo_sala import insert_tipo_sala

# try:
#     dc.slct_disciplinas_controller()
# except Exception as e:
#     print(f"Erro: {e}")

# try:
#     data = {"nome": "TESTE"}
#     fc.insrt_formatos_controller(data)
# except Exception as e:
#     print(f"Erro: {e}")

# insert_formatos()
# insrt_especialidade()
# teste_conexao_bd()
insert_tipo_sala()