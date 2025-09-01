"""Kardex form module."""

from time import sleep

from uiautomation import ListItemControl

from ...models.kardex.number import KardexNumber
from ...models.kardex.type import KardexType
from .._base.form import BaseForm
from .controls import KARDEX_WINDOW, NUMBER_EDIT, TYPE_BUTTON, TYPE_COMBO_BOX, TYPE_LIST


class KardexForm(BaseForm):
    """Kardex form class."""

    _window = KARDEX_WINDOW

    @staticmethod
    def get_kardex_type() -> KardexType:
        """Returns the kardex type."""
        type_combo_box = TYPE_COMBO_BOX.GetValuePattern()
        type_combo_box_value = type_combo_box.Value
        return KardexType(type_combo_box_value)

    @classmethod
    def set_kardex_type(cls, value: KardexType) -> None:
        """Sets the kardex type."""
        if not isinstance(value, KardexType):
            raise ValueError("Kardex type must be an instance of KardexType.")
        current_kardex_type: KardexType = cls.get_kardex_type()
        if value == current_kardex_type:
            return None
        kardex_types: frozenset[KardexType] = cls.get_kardex_types()
        if value not in kardex_types:
            options: tuple[str, ...] = tuple(v.root for v in kardex_types)
            options_message: str = "Available options: " + ", ".join(options) + "."
            raise ValueError(f"Unknown kardex type {value.root}. {options_message}")
        if cls._has_type_list():
            cls._invoke_type_button()
        assert TYPE_COMBO_BOX.Select(value.root)
        new_kardex_type = cls.get_kardex_type()
        assert new_kardex_type == value
        return cls._wait_for_update()

    @staticmethod
    def get_kardex_number() -> KardexNumber | None:
        """Returns the kardex number if it exists."""
        number_edit = NUMBER_EDIT.GetValuePattern()
        if number_edit_value := number_edit.Value:
            return KardexNumber(number_edit_value)
        return None

    @classmethod
    def set_kardex_number(cls, value: KardexNumber) -> None:
        """Sets the kardex number."""
        if not isinstance(value, KardexNumber):
            raise ValueError("Kardex number must be an instance of KardexNumber.")
        current_kardex_number: KardexNumber | None = cls.get_kardex_number()
        if current_kardex_number and value == current_kardex_number:
            return None
        str_kardex_number: str = str(value.root)
        number_edit = NUMBER_EDIT.GetValuePattern()
        assert number_edit.SetValue(str_kardex_number)
        assert (new_kardex_number := cls.get_kardex_number())
        assert new_kardex_number == value
        NUMBER_EDIT.SendKeys("{ENTER}")
        return cls._wait_for_update()
        # TODO: Check if kardex number not found error.

    @classmethod
    def get_kardex_types(cls) -> frozenset[KardexType]:
        """Returns the kardex types."""
        ktl_items: tuple[ListItemControl, ...] = cls._get_kardex_type_list_items()
        kardex_types: frozenset[KardexType]
        kardex_types = frozenset(KardexType(item.Name) for item in ktl_items)
        assert len(kardex_types) == len(ktl_items)
        return kardex_types

    @classmethod
    def _get_kardex_type_list_items(cls) -> tuple[ListItemControl, ...]:
        """Gets the kardex type list items. Each instance can be selected just by calling the Select method on its SelectionItemPattern."""
        if not cls._has_type_list():
            cls._invoke_type_button()
        children = tuple(TYPE_LIST.GetChildren())
        list_items: tuple[ListItemControl, ...]
        list_items = tuple(c for c in children if isinstance(c, ListItemControl))
        assert len(children) == len(list_items)
        return list_items

    @staticmethod
    def _has_type_list() -> bool:
        """Returns whether the kardex type list exists."""
        return TYPE_LIST.Exists(maxSearchSeconds=0)

    @staticmethod
    def _invoke_type_button() -> None:
        """Invokes the type button."""
        type_button = TYPE_BUTTON.GetInvokePattern()
        assert type_button.Invoke()
        return None

    @staticmethod
    def _wait_for_update() -> None:
        """
        Temporarily waits for the kardex data to update.

        This method introduces a 2-second delay to reduce the risk of subsequent
        actions failing due to incomplete UI updates. On average, the update takes
        about 1 second, but waits longer to ensure the UI is fully updated.

        TODO:
            Replace this fixed delay with an event-based or state-check mechanism
            to ensure reliability.
        """
        return sleep(2)
