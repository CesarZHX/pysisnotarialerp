from typing import overload

from pydantic import ConfigDict, PositiveInt, RootModel


class KardexNumber(RootModel[PositiveInt]):
    """Kardex number model."""

    model_config = ConfigDict(frozen=True)

    @overload
    def __init__(self, value: PositiveInt) -> None: ...
    @overload
    def __init__(self, value: str) -> None: ...
    def __init__(self, value: PositiveInt | str) -> None:
        """Initializes a new instance of the KardexNumber class."""
        return super().__init__(int(value))
