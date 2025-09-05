"""Base window module."""

from uiautomation import WindowControl


class BaseWindow:
    """Base window class."""

    _window: WindowControl

    @classmethod
    def exists(cls) -> bool:
        """Returns whether the window exists."""
        window = cls._window
        return window.Exists(maxSearchSeconds=0)

    @classmethod
    def wait_for(cls) -> None:
        """Waits for the window to appear."""
        window = cls._window
        assert window.Exists()
        return None

    @classmethod
    def close(cls) -> None:
        """Closes the window."""
        if not cls.exists():
            return None
        window = cls._window
        window_pattern = window.GetWindowPattern()
        assert window_pattern.Close()
        return None

    @classmethod
    def set_active(cls) -> None:
        """Sets the window to active."""
        window = cls._window
        if window.IsOffscreen:
            assert window.SetActive()
        return None


class TopLevelWindow(BaseWindow):
    """Top level window class."""

    @classmethod
    def set_topmost(cls) -> None:
        """Sets the window to topmost."""
        window = cls._window
        if not window.IsTopmost():
            assert window.SetTopmost()
        return None

    @classmethod
    def wait_for(cls) -> None:
        """Waits for the window to appear, set to active and set to topmost."""
        super().wait_for()
        cls.set_active()
        return cls.set_topmost()


class MandatoryWindow(BaseWindow):
    """Mandatory window class."""

    def __init__(self) -> None:
        """Initializes a new instance of the SubWindow class."""
        return self.wait_for()


class MandatoryTopLevelWindow(MandatoryWindow, TopLevelWindow):
    """Mandatory top level window class."""
