"""Kardex exceptions."""

from ....exceptions import SisNotarialErpException


class KardexException(SisNotarialErpException):
    """Base class for login exceptions."""


class KardexNotExistsError(KardexException):
    """Raised when the kardex does not exist."""
