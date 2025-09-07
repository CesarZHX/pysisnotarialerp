from ...exceptions import SisNotarialErpException


class DialogException(SisNotarialErpException):
    """Base class for combo box exceptions."""


class UnexpectedDialogMessageError(DialogException):
    """Unexpected dialog message error."""
