# from app.backend.modules.disciplinas.disciplinas_controller import (
#     DisciplinasController as dc
# )
# from app.backend.modules.formatos.formatos_controller import (
#     FormatosController as fc
# )
from scripts.insertions.insert_formatos import (
    insert_formatos
)   


# try:
#     dc.slct_disciplinas_controller()
# except Exception as e:
#     print(f"Erro: {e}")

# try:
#     data = {"nome": "TESTE"}
#     fc.insrt_formatos_controller(data)
# except Exception as e:
#     print(f"Erro: {e}")

insert_formatos()
