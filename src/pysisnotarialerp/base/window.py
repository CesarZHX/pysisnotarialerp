"""Base window module."""

from uiautomation import WindowControl


class BaseWindow:
    """Base window class."""

    _window: WindowControl

    def __init__(self) -> None:
        """Initializes a new instance of the Window class."""
        return self.wait()

    @classmethod
    def wait(cls) -> None:
        """Waits for the window to appear."""
        cls._window.Exists()
        return None

    @classmethod
    def exists(cls) -> bool:
        """Returns whether the window exists."""
        return cls._window.Exists(maxSearchSeconds=0)
