"""Login window module."""

from pathlib import Path
from subprocess import Popen

from pydantic import SecretStr

from ...base.window import BaseWindow
from ..main.window import MainWindow
from .controls import LOGIN_WINDOW, PASSWORD_EDIT, SUBMIT_BUTTON, USERNAME_EDIT
from .exceptions import raise_login_error


class LoginWindow(BaseWindow):
    """Login window class.
    - This class is designed to manage **a single instance** of the application.
    - If multiple instances are running, it will always attach to and control **only the first one it finds**.
    - Managing multiple instances is **not currently supported** (and may not be possible).
    - **Running the program more than once is not recommended**,
    since the library cannot guarantee which instance will be attached to, which may cause unexpected behavior.
    - **Creating multiple objects of this class is also not recommended**,
    because they will all try to access the same first instance found, which can lead to conflicts.
    """

    _window = LOGIN_WINDOW
    _executable_file: Path
    _popen: Popen | None = None

    def __init__(self, executable_file_path: Path | str) -> None:
        """Initializes a new instance of the LoginWindow class."""
        self._executable_file: Path = Path(executable_file_path)
        if not self._executable_file.is_file():
            raise ValueError("executable must be a valid file path.")
        return super().__init__()

    def login(self, username: str, password: SecretStr) -> MainWindow:
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
        if not self.exists():
            self._popen = Popen(self._executable_file)
        self.wait_for()
        username_edit = USERNAME_EDIT.GetValuePattern()
        username_edit.SetValue(username)
        password_edit = PASSWORD_EDIT.GetValuePattern()
        password_edit.SetValue(password.get_secret_value())
        submit_button = SUBMIT_BUTTON.GetInvokePattern()
        submit_button.Invoke()
        if self.exists():
            raise_login_error()
        return MainWindow()
