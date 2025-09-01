"""Sis Notarial ERP module."""

from pathlib import Path
from subprocess import Popen

from pydantic import SecretStr

from .forms.login.form import LoginForm
from .forms.main.form import MainForm


class SisNotarialERP:
    """`SisNotarialERP` class.
    - This class is designed to manage **a single instance** of the application.
    - If multiple instances are running, it will always attach to and control **only the first one it finds**.
    - Managing multiple instances is **not currently supported** (and may not be possible).
    - **Running the program more than once is not recommended**,
    since the library cannot guarantee which instance will be attached to, which may cause unexpected behavior.
    - **Creating multiple `SisNotarialERP` controller objects is also not recommended**,
    because they will all try to access the same first instance found, which can lead to conflicts.
    """

    def __init__(self, executable_file_path: Path | str) -> None:
        """Initializes a new instance of the SisNotarialERP class."""
        self._executable_file: Path = Path(executable_file_path)
        if not self._executable_file.is_file():
            raise ValueError("executable must be a valid file path.")
        self._popen: Popen | None = None
        return None

    def login(self, username: str, password: SecretStr) -> MainForm:
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
        if not (MainForm.exists() or LoginForm.exists()):
            self._popen = Popen(self._executable_file)
        login_form: LoginForm = LoginForm()
        return login_form.login(username, password)
