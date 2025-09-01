"""Login exceptions."""

from ...exceptions import SisNotarialErpException
from .controls import WRONG_PASSWORD_TEXT


class LoginException(SisNotarialErpException):
    """Base class for login exceptions."""


class WrongPasswordError(LoginException):
    """Raised when the password is incorrect."""


def raise_login_error() -> None:
    """Raises the corresponding login error."""
    if WRONG_PASSWORD_TEXT.Exists(maxSearchSeconds=0):
        raise WrongPasswordError
    # TODO: Check for no user error.
    # TODO: Check for no password error.
    # TODO: Check for unregistered user error.
    # TODO: Check for too long user error.
    raise LoginException
