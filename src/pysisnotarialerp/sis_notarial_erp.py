"""Sis Notarial ERP window controls."""

from uiautomation import ButtonControl, ToolBarControl, WindowControl

_WINDOW_NAME: str = f"SIS NOTARIAL ERP{' '*143}"
WINDOW: WindowControl = WindowControl(searchDepth=1, Name=_WINDOW_NAME)


_TOOL_BAR_NAME: str = "ToolStrip1"
_TOOL_BAR: ToolBarControl = WINDOW.ToolBarControl(searchDepth=1, Name=_TOOL_BAR_NAME)


KARDEX_BUTTON: ButtonControl
_KARDEX_BUTTON_NAME: str = "KARDEX (F1)"
KARDEX_BUTTON = _TOOL_BAR.ButtonControl(searchDepth=1, Name=_KARDEX_BUTTON_NAME)
