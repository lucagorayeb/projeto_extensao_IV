from backend.modules.turma.turma_repository import TurmaRepository
from backend.modules.turma.turma_exception import ScheduleConflict, ProfessorClassNumber, ProfessorScheduleConflict
from sqlalchemy.exc import IntegrityError

class TurmaService:

    def __init__(self):
        self.repo = TurmaRepository()

    def insrt_turma_service(self, data: dict) -> None:
        verifica_sala_dia_semana = self.__verifica_sala_dia_semana_service(data['fk_sala'], data['fk_dia_semana'])
        if verifica_sala_dia_semana > 0:
            raise ScheduleConflict("Essa sala já está ocupada nesse dia. Escolha outra sala ou outro dia da semana.")

        verifica_quant_turmas_professor = self.__verifica_quantidade_turmas_professor_service(data['fk_professor'])
        if verifica_quant_turmas_professor >= 5:
            raise ProfessorClassNumber("O limite de turmas (5) desse professor foi atingido.")

        verifica_professor_dia_semana = self.__verifica_professor_dia_semana_service(data['fk_professor'], data['fk_dia_semana'])
        if verifica_professor_dia_semana > 0:
            raise ProfessorScheduleConflict("O professor não pode dar mais de uma aula no mesmo dia.")
        
        self.__save(data)

    def __save(self, data: dict, turma_id: int | None = None) -> None:
        try:
            if turma_id is not None:
                self.repo.update({**data, "id": turma_id})
                return
            self.repo.insert(data)
        except IntegrityError as error:
            # A verificação prévia não impede duas requisições simultâneas.
            # A restrição UNIQUE é a garantia final no MySQL.
            args = getattr(error.orig, "args", ())
            if args and args[0] == 1062 and "uq_turma_sala_dia" in str(error.orig):
                raise ScheduleConflict("Essa sala já está ocupada nesse dia. Escolha outra sala ou outro dia da semana.") from error
            raise

    def updt_turma_service(self, data: dict, id: int) -> None:
        verifica_sala_dia_semana = self.__verifica_sala_dia_semana_service(data['fk_sala'], data['fk_dia_semana'], id)
        if verifica_sala_dia_semana > 0:
            raise ScheduleConflict("Essa sala já está ocupada nesse dia. Escolha outra sala ou outro dia da semana.")

        verifica_quant_turmas_professor = self.__verifica_quantidade_turmas_professor_service(data['fk_professor'], id)
        if verifica_quant_turmas_professor >= 5:
            raise ProfessorClassNumber("O limite de turmas (5) desse professor foi atingido.")

        verifica_professor_dia_semana = self.__verifica_professor_dia_semana_service(data['fk_professor'], data['fk_dia_semana'], id)
        if verifica_professor_dia_semana > 0:
            raise ProfessorScheduleConflict("O professor não pode dar mais de uma aula no mesmo dia.")
        
        self.__save(data, id)

    def del_turma_service(self, id: int) -> None:
        self.repo.delete(id)

    def slct_turma_service(self) -> list:
        data = self.repo.select()
        return self.__data_treatment(data)

    def slct_by_id_turma_service(self, id: int) -> list:
        data = self.repo.select_by_id(id)
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

    def __verifica_sala_dia_semana_service(self, sala_id: int, dia_semana_id: int, turma_id: int | None = None) -> int:
        return self.repo.verifica_sala_dia_semana(sala_id, dia_semana_id, turma_id)

    def __verifica_quantidade_turmas_professor_service(self, professor_id: int, turma_id: int | None = None) -> int:
        return self.repo.verifica_quantidade_turmas_professor(professor_id, turma_id)

    def __verifica_professor_dia_semana_service(self, professor_id: int, dia_semana_id: int, turma_id: int | None = None) -> int:
        return self.repo.verifica_professor_dia_semana(professor_id, dia_semana_id, turma_id)