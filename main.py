# from app.backend.modules.disciplinas.disciplinas_controller import (
#     DisciplinasController as dc
# )
# from app.backend.modules.formato.formato_controller import FormatoController
# from tests.db_connection_test import teste_conexao_bd
# from scripts.insertions.insert_formato import insert_formatos
# from scripts.insertions.insert_especialidade import insrt_especialidade
# from scripts.insertions.insert_tipo_sala import insert_tipo_sala
from app.backend.modules.sala.sala_controller import SalaController
from app.backend.modules.tipo_sala.tipo_sala_controller import TipoSalaController
# from scripts.insertions.insert_sala import insert_sala
from app.router.web import app
from sqlalchemy.exc import SQLAlchemyError, OperationalError, IntegrityError



# try:
# fc = FormatoController()
# dados = fc.slct_formato_controller()
# print(dados)

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
# print(insert_sala())

# c = SalaController()
# dados = c.slct_sala_controller()
# dados = c.slct_by_id_sala_controller(14)
# print(dados)

# c.slct_sala_controller()
# c.slct_by_id_sala_controller(14)

# try:
#     c.insrt_sala_controller({"nome": "Sala 293", "limite_alunos": 35, "fk_tipo_sala": 4})
# except SQLAlchemyError as e: 
#     print(e)
# except OperationalError as e:
#     print(e)
# except IntegrityError as e:
#     print(e)


# c.updt_sala_controller({'nome': 'Sala 365', 'limite_alunos': 35, 'fk_tipo_sala': 1}, 14)
# c.del_sala_controller(14)


ts = TipoSalaController()
# teste = ts.slct_tipo_sala_controller()
# teste = ts.slct_by_id_tipo_sala_controller(2)
# print(teste)
# ts.insrt_tipo_sala_controller(data="teste")
# ts.updt_tipo_sala_controller({"nome": "teste1"}, 5)
# ts.del_tipo_sala_controller(5)