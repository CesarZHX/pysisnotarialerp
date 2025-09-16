"""Kardex window module."""

from time import sleep

from ....base.window import MandatoryWindow
from ....models.kardex.number import KardexNumber
from ....models.kardex.type import KardexType
from .controls import (
    ACCEPT_BUTTON,
    KARDEX_NOT_EXIST_TEXT,
    KARDEX_WINDOW,
    NEW_PUBLIC_RECORDS_TEXT,
    NUMBER_EDIT,
    PUBLIC_RECORDS_BUTTON,
    TYPE_COMBO_BOX,
)
from .exceptions import KardexNotExistsError
from .public_records.controls import DIALOG
from .public_records.window import PublicRecordsWindow


class KardexWindow(MandatoryWindow):
    """Kardex window class."""

    _window = KARDEX_WINDOW

    def __init__(self) -> None:
        """Initializes a new instance of the KardexWindow class."""
        super().__init__()
        return self.close_subwindows()

    @staticmethod
    def get_kardex_types() -> tuple[KardexType, ...]:
        """Returns the kardex types."""
        return tuple(KardexType(option) for option in TYPE_COMBO_BOX.options)

    @staticmethod
    def get_kardex_type() -> KardexType:
        """Returns the kardex type."""
        return KardexType(TYPE_COMBO_BOX.value)

    @classmethod
    def set_kardex_type(cls, value: KardexType) -> None:
        """Sets the kardex type."""
        if not isinstance(value, KardexType):
            raise ValueError("Kardex type must be an instance of KardexType.")
        TYPE_COMBO_BOX.value = value.root
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
        cls._wait_for_update()
        """TODO: To prevent KARDEX_NOT_EXIST_TEXT from even appearing, compare
        the kardex with the lastest kardex of its type before continuing."""
        if KARDEX_NOT_EXIST_TEXT.Exists(maxSearchSeconds=0):
            ACCEPT_BUTTON.GetInvokePattern().Invoke()
            raise KardexNotExistsError
        return None

    @staticmethod
    def _wait_for_update() -> None:
        """
        Temporarily waits for the kardex data to update.

        This method introduces a 2-second delay to reduce the risk of subsequent
        actions failing due to incomplete UI updates. On average, the update takes
        about 1 second, but waits longer to ensure the UI is fully updated.

        TODO: Replace this fixed delay with an event-based or state-check
        mechanism to ensure reliability.
        """
        return sleep(2)

    @classmethod
    def go_to_public_records_panel(cls) -> None:
        if NEW_PUBLIC_RECORDS_TEXT.Exists(maxSearchSeconds=0):
            return None
        public_records_button = PUBLIC_RECORDS_BUTTON.GetInvokePattern()
        public_records_button.Invoke()
        return cls._wait_for_update()

    @classmethod
    def get_public_records_window(cls) -> PublicRecordsWindow:
        """Returns the public records window."""
        cls.go_to_public_records_panel()
        if not PublicRecordsWindow.exists():
            NEW_PUBLIC_RECORDS_TEXT.Click()
        return PublicRecordsWindow()

    @classmethod
    def get_record_window(cls) -> PublicRecordsWindow:
        """Returns the record window."""
        raise NotImplementedError

    @classmethod
    def close_subwindows(cls) -> None:
        """Closes the subwindows."""
        for subwindow in (PublicRecordsWindow,):
            subwindow.close()
        DIALOG.close()
        return None
