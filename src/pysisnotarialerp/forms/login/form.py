"""Login form module."""

from pydantic import SecretStr

from .._base.form import BaseForm
from ..main.form import MainForm
from .controls import (
    LOGIN_WINDOW,
    PASSWORD_EDIT,
    SUBMIT_BUTTON,
    USERNAME_EDIT,
    WRONG_PASSWORD_TEXT,
)
from .exceptions import LoginException, WrongPasswordError


class LoginForm(BaseForm):
    """Login form class."""

    _window = LOGIN_WINDOW

    @classmethod
    def login(cls, username: str, password: SecretStr) -> MainForm:
        """Logs in to the SIS Notarial ERP application.

        Args:
            username (str): Username to log in with.
            password (SecretStr): Password to log in with.

        Raises:
            LoginException: If login fails.
            WrongPasswordError: If the password is incorrect.

        Returns:
            WindowControl: The SIS Notarial ERP application window.
        """
        if MainForm.exists():
            return MainForm()
        USERNAME_EDIT.GetValuePattern().SetValue(username)
        PASSWORD_EDIT.GetValuePattern().SetValue(password.get_secret_value())
        SUBMIT_BUTTON.Click()
        if not cls.exists():
            return MainForm()
        if WRONG_PASSWORD_TEXT.Exists(maxSearchSeconds=0):
            raise WrongPasswordError
        raise LoginException
