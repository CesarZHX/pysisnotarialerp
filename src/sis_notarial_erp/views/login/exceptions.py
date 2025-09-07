"""Login exceptions."""

from ...exceptions import DatabaseException, SisNotarialErpException
from .controls import DIALOG


class LoginException(SisNotarialErpException):
    """Base class for login exceptions."""


class DatabaseLoginException(LoginException, DatabaseException):
    """Base class for database login exceptions."""


class EmptyUsernameError(LoginException):
    """Raised when there is no username."""


class EmptyPasswordError(LoginException):
    """Raised when there is no password."""


class UnregisteredUsernameError(LoginException):
    """Raised when there is no registered username."""


class UsernameTooLongError(DatabaseLoginException):
    """Raised when the username is too long."""


class WrongPasswordError(LoginException):
    """Raised when the password is incorrect."""


def raise_login_error() -> None:
    """Raises the corresponding login error."""
    if not DIALOG.exists():
        raise LoginException
    errors: list[LoginException] = list()
    message: str = DIALOG.get_value()
    error: LoginException = _get_login_error_by_message(message)
    errors.append(error)
    if isinstance(error, UsernameTooLongError):
        main_error: LoginException = _get_login_error_by_message(message)
        errors.append(main_error)
    assert not DIALOG.exists()
    if len(errors) == 1:
        raise errors[0]
    raise ExceptionGroup("Multiple login errors", errors)


def _get_login_error_by_message(message: str) -> LoginException:
    return _LOGIN_ERRORS.get(message, LoginException(message))


_LOGIN_ERRORS: dict[str, LoginException] = {
    "INGRESE EL USUARIO": EmptyUsernameError(),
    "INGRESE SU CLAVE": EmptyPasswordError(),
    "Personal no registrado": UnregisteredUsernameError(),
    "Data too long for column 'kardex' at row 1": UsernameTooLongError(),
    "Clave Incorrecta": WrongPasswordError(),
}
