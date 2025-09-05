"""Base window module."""

from uiautomation import WindowControl


class BaseWindow:
    """Base window class."""

    _window: WindowControl

    def __init__(self) -> None:
        """Initializes a new instance of the Window class."""
        self.wait_for()
        assert self._window.SetTopmost()
        return None

    @classmethod
    def wait_for(cls) -> None:
        """Waits for the window to appear."""
        assert cls._window.Exists()
        return None

    @classmethod
    def exists(cls) -> bool:
        """Returns whether the window exists."""
        return cls._window.Exists(maxSearchSeconds=0)
