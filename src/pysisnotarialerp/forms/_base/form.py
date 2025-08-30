"""Base form module."""

from uiautomation import WindowControl


class BaseForm:
    """Base form class."""

    _window: WindowControl

    def __init__(self) -> None:
        self.wait()
        return None

    @classmethod
    def wait(cls) -> None:
        """Waits for the window form to appear."""
        cls._window.Exists()
        return None

    @classmethod
    def exists(cls) -> bool:
        """Returns whether the window form exists."""
        return cls._window.Exists(maxSearchSeconds=0)
