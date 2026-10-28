from datetime import datetime, time
from sqlalchemy import INT, VARCHAR, String, TIMESTAMP, Numeric, TIME
from sqlalchemy.orm import DeclarativeBase, mapped_column, registry
from decimal import Decimal
from typing_extensions import Annotated

str_30 = Annotated[str, 30]
str_50 = Annotated[str, 50]
num_12_4 = Annotated[Decimal, 12]
num_6_2 = Annotated[Decimal, 6]
num_5_2 = Annotated[Decimal, 5]
initpk = Annotated[int, mapped_column(primary_key=True)]
timestamp = Annotated[datetime, mapped_column(nullable=False)]


class DefaultModel(DeclarativeBase):

    registry = registry(
        type_annotation_map = {
            int: INT,
            datetime: TIMESTAMP(timezone=True),
            str: String().with_variant(VARCHAR(255), "mysql"),
            str_30: String(30),
            str_50: String(50),
            num_12_4: Numeric(12, 4),
            num_6_2: Numeric(6, 2),
            time: TIME(timezone=True),
            num_5_2: Numeric(5, 2)
        }
    )