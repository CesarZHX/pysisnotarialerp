"""Main form module."""

from .._base.form import BaseForm
from ..kardex.form import KardexForm
from .controls import KARDEX_BUTTON, MAIN_WINDOW


class MainForm(BaseForm):
    """Main form class."""

    _window = MAIN_WINDOW

    @staticmethod
    def get_kardex_form() -> KardexForm:
        """Returns the kardex form."""
        if KardexForm.exists():
            return KardexForm()
        KARDEX_BUTTON.SetFocus()
        KARDEX_BUTTON.Click()
        return KardexForm()
