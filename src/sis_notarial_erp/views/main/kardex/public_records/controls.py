"""Public records controls."""

from .....models.combo_box.model import ComboBox
from ....main.kardex.controls import MAIN_WINDOW

_PR_WINDOW = MAIN_WINDOW.WindowControl(searchDepth=1, AutomationId="FrmRRPP")
PUBLIC_RECORDS_WINDOW = _PR_WINDOW

DOCUMENT_DATE_PANE = _PR_WINDOW.PaneControl(searchDepth=1, AutomationId="dpfechaRP")
DOCUMENT_TIME_EDIT = _PR_WINDOW.EditControl(searchDepth=1, AutomationId="txHoraReg")
_RS_COMBO_BOX = _PR_WINDOW.ComboBoxControl(searchDepth=1, AutomationId="cbEstadoRP")
REGISTRY_STATUS_COMBO_BOX: ComboBox = ComboBox(_RS_COMBO_BOX)
_RO_COMBO_BOX = _PR_WINDOW.ComboBoxControl(searchDepth=1, AutomationId="cbORegistral")
REGISTRY_OFFICE_COMBO_BOX: ComboBox = ComboBox(_RO_COMBO_BOX)
_RA_COMBO_BOX = _PR_WINDOW.ComboBoxControl(searchDepth=1, AutomationId="cbRegistral")
REGISTRY_AREA_COMBO_BOX: ComboBox = ComboBox(_RA_COMBO_BOX)
TITLE_NUMBER_EDIT = _PR_WINDOW.EditControl(searchDepth=1, AutomationId="txTituloRP")
_RFN_EDIT = _PR_WINDOW.EditControl(searchDepth=1, AutomationId="txPartidaRP")
REGISTRY_FILE_NUMBER_EDIT = _RFN_EDIT
_RRN_EDIT = _PR_WINDOW.EditControl(searchDepth=1, AutomationId="txAsientoRP")
REGISTRY_RECORD_NUMBER_EDIT = _RRN_EDIT
DEADLINE_DATE_EDIT = _PR_WINDOW.EditControl(searchDepth=1, AutomationId="txFechaPlazo")
TIVE_EDIT = _PR_WINDOW.EditControl(searchDepth=1, AutomationId="txTive")
_PS_COMBO_BOX = _PR_WINDOW.ComboBoxControl(searchDepth=1, AutomationId="cbDescargo")
PAYMENT_STATUS_COMBO_BOX: ComboBox = ComboBox(_PS_COMBO_BOX)
TOTAL_EDIT = _PR_WINDOW.EditControl(searchDepth=1, AutomationId="txPagoRP")
AON_EDIT = _PR_WINDOW.EditControl(searchDepth=1, AutomationId="txOrden")
ASSOCIATED_ORDER_NUMBER_EDIT = AON_EDIT
SAVE_BUTTON = _PR_WINDOW.ButtonControl(searchDepth=1, AutomationId="btGrabar")
_PM_CHECK_RADIO = _PR_WINDOW.RadioButtonControl(searchDepth=1, AutomationId="rbCheque")
PAYMENT_METHOD_CHECK_RADIO_BUTTON = _PM_CHECK_RADIO  # NOTE: Select Pattern > Select
_PM_CASH_RADIO = _PR_WINDOW.RadioButtonControl(searchDepth=1, AutomationId="rbEfectivo")
PAYMENT_METHOD_CASH_RADIO_BUTTON = _PM_CASH_RADIO  # NOTE: Select Pattern > Select
_PM_CARD_RADIO = _PR_WINDOW.RadioButtonControl(searchDepth=1, AutomationId="rbTarjeta")
PAYMENT_METHOD_CARD_RADIO_BUTTON = _PM_CARD_RADIO  # NOTE: Select Pattern > Select
