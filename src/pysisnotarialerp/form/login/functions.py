"""Login functions."""

from pydantic import SecretStr

from ...sis_notarial_erp.controls import WINDOW
from .controls import (
    LOGIN_WINDOW,
    PASSWORD_EDIT,
    SUBMIT_BUTTON,
    USERNAME_EDIT,
    WRONG_PASSWORD_TEXT,
)
from .exceptions import LoginException, WrongPasswordError


def login(username: str, password: SecretStr) -> None:
    """Logs in to the SIS Notarial ERP application.

    Args:
        username (str): Username to log in with.
        password (SecretStr): Password to log in with.

    Raises:
        LoginException: If login fails.
        WrongPasswordError: If the password is incorrect.
    """
    if WINDOW.Exists(maxSearchSeconds=0):
        return None
    LOGIN_WINDOW.SetTopmost()
    USERNAME_EDIT.GetValuePattern().SetValue(username)
    PASSWORD_EDIT.GetValuePattern().SetValue(password.get_secret_value())
    SUBMIT_BUTTON.Click()
    if not SUBMIT_BUTTON.Exists(maxSearchSeconds=0) and WINDOW.Exists():
        return None
    if WRONG_PASSWORD_TEXT.Exists(maxSearchSeconds=0):
        raise WrongPasswordError
    raise LoginException
