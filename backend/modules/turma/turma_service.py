from backend.modules.turma.turma_repository import TurmaRepository

class TurmaService:

    def __init__(self):
        self.repo = TurmaRepository()

    def insrt_turma_service(self, data: dict) -> None:
        self.repo.insert(data)

    def updt_turma_service(self, data: dict, id: int) -> None:
        data.update({"id": id})
        self.repo.update(data)

    def del_turma_service(self, id: int) -> None:
        self.repo.delete(id)

    def slct_turma_service(self) -> list:
        data = self.repo.select()
        return self.__data_treatment(data)

    def __data_treatment(self, data: list) -> list:
        normalized_data = []
        for d in data:
            normalized_data.append({
                'id': d.id,
                'fk_disciplina': d.fk_disciplina,
                'fk_disciplina_nome': d.fk_disciplina_nome,
                'fk_sala': d.fk_sala,
                'fk_sala_nome': d.fk_sala_nome,
                'fk_professor': d.fk_professor,
                'fk_professor_nome': d.fk_professor_nome,
                'fk_dia_semana': d.fk_dia_semana,
                'fk_dia_semana_nome': d.fk_dia_semana_nome,
                'carga_horaria': d.carga_horaria,
                'horario_inicio': d.horario_inicio,
                'horario_fim': d.horario_fim
            })
        return normalized_data

    def get_dias_semana_service(self) -> list:
        data = self.repo.get_dias_semana()
        return self.__dias_semana_treatment(data)

    def __dias_semana_treatment(self, data: list) -> list:
        normalized_data = []
        for d in data:
            normalized_data.append({
                'id': d.id,
                'nome': d.nome
            })
        return normalized_data