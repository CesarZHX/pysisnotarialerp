"""Main window module."""

from ...base.window import MandatoryTopLevelWindow
from .controls import KARDEX_BUTTON, MAIN_WINDOW
from .kardex.window import KardexWindow


class MainWindow(MandatoryTopLevelWindow):
    """Main window class."""

    _window = MAIN_WINDOW

    def __init__(self) -> None:
        """Initializes a new instance of the MainWindow class."""
        super().__init__()
        return self.maximize()

    @classmethod
    def maximize(cls) -> None:
        """Maximizes the main window."""
        window = cls._window
        if not window.IsMaximize():
            assert window.Maximize()
        return None

    @staticmethod
    def get_kardex_window() -> KardexWindow:
        """Returns the kardex form."""
        if KardexWindow.exists():
            return KardexWindow()
        kardex_button = KARDEX_BUTTON.GetInvokePattern()
        kardex_button.Invoke()
        return KardexWindow()

    @classmethod
    def unset_topmost(cls) -> None:
        """Unsets the topmost attribute of the main window."""
        window = cls._window
        if window.IsTopmost():
            assert window.SetTopmost(False)
        return None
