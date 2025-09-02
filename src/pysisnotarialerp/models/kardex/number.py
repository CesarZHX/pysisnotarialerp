"""Kardex number model module."""

from typing import Annotated, overload

from pydantic import ConfigDict, Field, PositiveInt, RootModel

PositiveUInt32 = Annotated[int, Field(ge=1, le=2_147_483_647)]


class KardexNumber(RootModel[PositiveUInt32]):
    """Kardex number model."""

    model_config = ConfigDict(frozen=True)

    @overload
    def __init__(self, value: PositiveInt) -> None: ...
    @overload
    def __init__(self, value: str) -> None: ...
    def __init__(self, value: PositiveInt | str) -> None:
        """Initializes a new instance of the KardexNumber class."""
        return super().__init__(int(value))
