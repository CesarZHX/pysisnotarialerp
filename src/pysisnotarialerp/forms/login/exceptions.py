"""Login exceptions."""

from ...exceptions import SisNotarialErpException


class LoginException(SisNotarialErpException):
    """Base class for login exceptions."""


class WrongPasswordError(LoginException):
    """Raised when the password is incorrect."""
