"""Public records controls."""

from .....models.combo_box.model import ComboBox
from ....main.kardex.controls import MAIN_WINDOW
from ..controls import _KARDEX_PANE

_PR_PANE = _KARDEX_PANE.PaneControl(searchDepth=1, AutomationId="pnRrpp")
PUBLIC_RECORDS_PANE = _PR_PANE

NEW_TEXT = _PR_PANE.TextControl(searchDepth=1, AutomationId="lbNuevoRp")


_PR_WINDOW = MAIN_WINDOW.WindowControl(searchDepth=1, AutomationId="FrmRRPP")
PUBLIC_RECORDS_WINDOW = _PR_WINDOW

DATE_PANE = _PR_WINDOW.PaneControl(searchDepth=1, AutomationId="dpfechaRP")
_RS_COMBO_BOX = _PR_WINDOW.ComboBoxControl(searchDepth=1, AutomationId="cbEstadoRP")
REGISTRY_STATE_COMBO_BOX: ComboBox = ComboBox(_RS_COMBO_BOX)
_RO_COMBO_BOX = _PR_WINDOW.ComboBoxControl(searchDepth=1, AutomationId="cbORegistral")
REGISTRY_OFFICE_COMBO_BOX: ComboBox = ComboBox(_RO_COMBO_BOX)
_RA_COMBO_BOX = _PR_WINDOW.ComboBoxControl(searchDepth=1, AutomationId="cbRegistral")
REGISTRY_AREA_COMBO_BOX: ComboBox = ComboBox(_RA_COMBO_BOX)

_PS_COMBO_BOX = _PR_WINDOW.ComboBoxControl(searchDepth=1, AutomationId="cbDescargo")
PAYMENT_STATE_COMBO_BOX: ComboBox = ComboBox(_PS_COMBO_BOX)
