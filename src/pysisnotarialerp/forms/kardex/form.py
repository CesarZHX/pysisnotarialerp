"""Kardex form module."""

from .._base.form import BaseForm
from .controls import KARDEX_WINDOW, NUMBER_EDIT, TYPE_COMBO_BOX, TYPE_LIST


class KardexForm(BaseForm):
    """Kardex form class."""

    _window = KARDEX_WINDOW
    _number_edit = NUMBER_EDIT
    _type_combo_box = TYPE_COMBO_BOX
    _type_list = TYPE_LIST
