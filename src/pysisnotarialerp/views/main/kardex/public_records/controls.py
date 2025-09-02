"""Public records controls."""

from ....main.kardex.controls import MAIN_WINDOW
from ..controls import _KARDEX_PANE

RRPP_WINDOW = MAIN_WINDOW.WindowControl(searchDepth=1, AutomationId="FrmRRPP")
PUBLIC_RECORDS_WINDOW = RRPP_WINDOW
RRPP_PANE = _KARDEX_PANE.PaneControl(searchDepth=1, AutomationId="pnRrpp")
PUBLIC_RECORDS_PANE = RRPP_PANE

DATE_PANE = RRPP_WINDOW.PaneControl(searchDepth=1, AutomationId="dpfechaRP")
NEW_TEXT = RRPP_PANE.TextControl(searchDepth=1, AutomationId="lbNuevoRp")
