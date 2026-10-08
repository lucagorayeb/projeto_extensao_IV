from ..base_modal import BaseModal
from typing import (
    List,
    Optional
)
from sqlalchemy import (
    relationship,
    String
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    ForeignKey
)

class SalaModal(BaseModal):

    __tablename__ = "sala"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[int] = mapped_column(String(30))
