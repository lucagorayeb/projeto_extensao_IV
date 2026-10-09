from ..base_modal.modal import (
    BaseModal,
    mapped_column,
    Mapped,
    ForeignKey as fk,
    initpk,
    str_30,
    timestamp
)

# from ..base_modal.modal import type_annotation_map as t, intpk, timestamp


class SalaModal(BaseModal):

    teste = BaseModal()

    __tablename__ = "sala"

    id: Mapped[initpk] 
    nome: Mapped[str_30]
    limite_alunos: Mapped[int] = mapped_column(nullable=False)
    fk_tipo_sala:  Mapped[int] = mapped_column(fk("tipo_sala.id"), nullable=False )
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp]
