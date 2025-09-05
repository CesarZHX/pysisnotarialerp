"""Login exceptions."""

from ...exceptions import SisNotarialErpException
from ...helpers.get_error_messages import get_error_messages
from .controls import LOGIN_WINDOW


def raise_login_error() -> None:
    """Raises the corresponding login error."""
    if not (messages := get_error_messages(LOGIN_WINDOW)):
        raise LoginException
    errors: tuple[LoginException, ...] = tuple(_get_login_error(m) for m in messages)
    if len(errors) == 1:
        raise errors[0]
    raise ExceptionGroup("Multiple login errors", errors)


class LoginException(SisNotarialErpException):
    """Base class for login exceptions."""


class EmptyUsernameError(LoginException):
    """Raised when there is no username."""


class EmptyPasswordError(LoginException):
    """Raised when there is no password."""


class UnregisteredUsernameError(LoginException):
    """Raised when there is no registered username."""


class UsernameTooLongError(LoginException):
    """Raised when the username is too long."""


class WrongPasswordError(LoginException):
    """Raised when the password is incorrect."""


def _get_login_error(error_message: str) -> LoginException:
    return _LOGIN_ERRORS.get(error_message, LoginException(error_message))


_LOGIN_ERRORS: dict[str, LoginException] = {
    "INGRESE EL USUARIO": EmptyUsernameError(),
    "INGRESE SU CLAVE": EmptyPasswordError(),
    "Personal no registrado": UnregisteredUsernameError(),
    "Data too long for column 'kardex' at row 1": UsernameTooLongError(),
    "Clave Incorrecta": WrongPasswordError(),
}
