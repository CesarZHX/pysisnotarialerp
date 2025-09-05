"""Base window module."""

from uiautomation import WindowControl


class BaseWindow:
    """Base window class."""

    _window: WindowControl

    @classmethod
    def exists(cls) -> bool:
        """Returns whether the window exists."""
        return cls._window.Exists(maxSearchSeconds=0)

    @classmethod
    def set_topmost(cls) -> None:
        """Sets the window to topmost."""
        assert cls._window.SetTopmost()
        return None

    @classmethod
    def wait_for(cls) -> None:
        """Waits for the window to appear."""
        assert cls._window.Exists()
        return cls.set_topmost()


class MandatoryWindow(BaseWindow):
    """Mandatory window class."""

    def __init__(self) -> None:
        """Initializes a new instance of the MandatoryWindow class."""
        return self.wait_for()
