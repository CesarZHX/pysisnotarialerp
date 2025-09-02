"""Sis Notarial ERP controls."""

from uiautomation import WindowControl

MAIN_WINDOW = WindowControl(searchDepth=1, Name=f"SIS NOTARIAL ERP{' '*143}")

_MAIN_PANE_NAME: str = 'Ingrese el tipo de cambio y presione "ENTER".'
_MAIN_PANE = MAIN_WINDOW.PaneControl(searchDepth=1, Name=_MAIN_PANE_NAME)
_TOOL_STRIP = MAIN_WINDOW.ToolBarControl(searchDepth=1, Name="ToolStrip1")

KARDEX_BUTTON = _TOOL_STRIP.ButtonControl(searchDepth=1, Name="KARDEX (F1)")
