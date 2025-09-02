"""Kardex type model module."""

from pydantic import ConfigDict, RootModel, field_validator

_STR_KARDEX_TYPES: tuple[str, ...]
_STR_KARDEX_TYPES = ("KA", "EX", "PT", "GM", "TE", "TV", "CC", "SK", "DP")
_KNOWN_KARDEX_TYPES: frozenset[str] = frozenset(_STR_KARDEX_TYPES)
assert len(_STR_KARDEX_TYPES) == len(_KNOWN_KARDEX_TYPES)


class KardexType(RootModel[str]):
    """Kardex type model."""

    model_config = ConfigDict(frozen=True)

    @field_validator("root")
    @classmethod
    def validate_kardex(cls, value: str) -> str:
        """Validates the kardex type."""
        stripped_value: str = value.strip()
        if len(stripped_value) != 2:
            raise ValueError("Kardex must be exactly 2 characters long")
        if not stripped_value.isalpha():
            raise ValueError("Kardex must contain only alphabetic characters")
        upper_value: str = stripped_value.upper()
        assert upper_value in _KNOWN_KARDEX_TYPES
        return upper_value


KARDEX_TYPES: frozenset[KardexType]
KARDEX_TYPES = frozenset(KardexType(skt) for skt in _STR_KARDEX_TYPES)
