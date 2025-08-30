"""Login exceptions."""

from ...sis_notarial_erp.exceptions import SisNotarialErpException


class LoginException(SisNotarialErpException):
    """Base class for login exceptions."""


class WrongPasswordError(LoginException):
    """Raised when the password is incorrect."""
