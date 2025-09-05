"""Login controls."""

from uiautomation import WindowControl

LOGIN_WINDOW = WindowControl(searchDepth=1, RegexName="ACCESO AL ERP NOTARIAL SIS")

_GROUP_BOX = LOGIN_WINDOW.GroupControl(searchDepth=1, AutomationId="gbLogin")
USERNAME_EDIT = _GROUP_BOX.EditControl(searchDepth=1, AutomationId="txUsuario")
PASSWORD_EDIT = _GROUP_BOX.EditControl(searchDepth=1, AutomationId="txClave")
SUBMIT_BUTTON = _GROUP_BOX.ButtonControl(searchDepth=1, AutomationId="btIngreso")
