"""Kardex controls."""

from ..main.controls import _PANE

KARDEX_WINDOW = _PANE.WindowControl(searchDepth=1, AutomationId="FrmKardex")
_TOOL_STRIP = KARDEX_WINDOW.ToolBarControl(searchDepth=1, AutomationId="ToolStrip1")
TYPE_COMBO_BOX = _TOOL_STRIP.ComboBoxControl(searchDepth=1, Name="")
TYPE_BUTTON = TYPE_COMBO_BOX.ButtonControl(searchDepth=1, Name="Abrir")
TYPE_LIST = TYPE_COMBO_BOX.ListControl(searchDepth=1, ClassName="ComboLBox")
NUMBER_EDIT = _TOOL_STRIP.EditControl(searchDepth=1, Name="")
