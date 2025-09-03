"""Kardex controls."""

from ....models.combo_box.model import ComboBox
from ...main.controls import _MAIN_PANE, MAIN_WINDOW

KARDEX_WINDOW = _MAIN_PANE.WindowControl(searchDepth=1, AutomationId="FrmKardex")
_KARDEX_PANE = KARDEX_WINDOW.PaneControl(searchDepth=1, AutomationId="pnPanel")

_TOOL_STRIP = KARDEX_WINDOW.ToolBarControl(searchDepth=1, AutomationId="ToolStrip1")
_TYPE_COMBO_BOX = _TOOL_STRIP.ComboBoxControl(searchDepth=1, Name="")
TYPE_COMBO_BOX: ComboBox = ComboBox(_TYPE_COMBO_BOX)
NUMBER_EDIT = _TOOL_STRIP.EditControl(searchDepth=1, Name="")

_OPTIONS_GROUP = KARDEX_WINDOW.GroupControl(searchDepth=1, Name="Opciones")
RECORD_BUTTON = _OPTIONS_GROUP.ButtonControl(searchDepth=1, AutomationId="btRegistro")
PR_BUTTON = _OPTIONS_GROUP.ButtonControl(searchDepth=1, AutomationId="btRrpp")
PUBLIC_RECORDS_BUTTON = PR_BUTTON

_INFO_WINDOW = MAIN_WINDOW.WindowControl(searchDepth=1, Name="SIS NOTARIAL ERP")
ACCEPT_BUTTON = _INFO_WINDOW.ButtonControl(searchDepth=1, Name="Aceptar")
_KNER_NAME: str = "EL Número de Kardex no existe"
KARDEX_NOT_EXIST_TEXT = _INFO_WINDOW.TextControl(searchDepth=1, Name=_KNER_NAME)
