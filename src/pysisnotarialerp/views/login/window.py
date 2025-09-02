"""Login window module."""

from pydantic import SecretStr

from ...base.window import BaseWindow
from ..main.window import MainWindow
from .controls import LOGIN_WINDOW, PASSWORD_EDIT, SUBMIT_BUTTON, USERNAME_EDIT
from .exceptions import raise_login_error


class LoginWindow(BaseWindow):
    """Login window class."""

    _window = LOGIN_WINDOW

    @classmethod
    def login(cls, username: str, password: SecretStr) -> MainWindow:
        """Logs in to the SIS Notarial ERP application.

        Args:
            username (str): Username to log in with.
            password (SecretStr): Password to log in with.

        Raises:
            LoginException: If login fails.

        Returns:
            WindowControl: The SIS Notarial ERP application window.
        """
        if MainWindow.exists():
            return MainWindow()
        username_edit = USERNAME_EDIT.GetValuePattern()
        username_edit.SetValue(username)
        password_edit = PASSWORD_EDIT.GetValuePattern()
        password_edit.SetValue(password.get_secret_value())
        submit_button = SUBMIT_BUTTON.GetInvokePattern()
        submit_button.Invoke()
        if cls.exists():
            raise_login_error()
        return MainWindow()
