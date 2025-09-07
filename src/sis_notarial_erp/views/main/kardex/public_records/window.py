"""Public Records window module."""

from datetime import date as Date
from datetime import datetime as Datetime
from datetime import time as Time
from decimal import Decimal
from time import sleep

from .....base.window import MandatoryTopLevelWindow
from .controls import (
    ASSOCIATED_ORDER_NUMBER_EDIT,
    DEADLINE_DATE_EDIT,
    DIALOG,
    DOCUMENT_DATE_PANE,
    DOCUMENT_TIME_EDIT,
    PAYMENT_METHOD_CARD_RADIO_BUTTON,
    PAYMENT_METHOD_CASH_RADIO_BUTTON,
    PAYMENT_METHOD_CHECK_RADIO_BUTTON,
    PAYMENT_STATUS_COMBO_BOX,
    PUBLIC_RECORDS_WINDOW,
    REGISTRY_AREA_COMBO_BOX,
    REGISTRY_FILE_NUMBER_EDIT,
    REGISTRY_OFFICE_COMBO_BOX,
    REGISTRY_RECORD_NUMBER_EDIT,
    REGISTRY_STATUS_COMBO_BOX,
    SAVE_BUTTON,
    TITLE_NUMBER_EDIT,
    TIVE_EDIT,
    TOTAL_EDIT,
)

_DATE_FORMAT: str = "%d/%m/%Y"
_TIME_FORMAT: str = "%H:%M"


class PublicRecordsWindow(MandatoryTopLevelWindow):
    """Public Records window class."""

    _window = PUBLIC_RECORDS_WINDOW

    @staticmethod
    def get_document_date() -> Date:
        """Returns the document date as a Date."""
        str_date: str = DOCUMENT_DATE_PANE.Name
        datetime: Datetime = Datetime.strptime(str_date, _DATE_FORMAT)
        return datetime.date()

    @classmethod
    def set_document_date(cls, value: Date) -> None:
        """Sets the document date."""
        if not isinstance(value, Date):
            raise ValueError("Document date must be a datetime.date.")
        current_document_date: Date = cls.get_document_date()
        if current_document_date == value:
            return None
        str_date: str = value.strftime(_DATE_FORMAT)
        stripped_date: str = str_date.lstrip("0")
        DOCUMENT_DATE_PANE.SendKeys(stripped_date)
        new_document_date: Date = cls.get_document_date()
        assert new_document_date == value
        return None

    @staticmethod
    def get_document_time() -> Time:
        """Returns the document time."""
        document_time_edit = DOCUMENT_TIME_EDIT.GetValuePattern()
        str_time: str = document_time_edit.Value
        datetime: Datetime = Datetime.strptime(str_time, _TIME_FORMAT)
        return datetime.time()

    @classmethod
    def set_document_time(cls, value: Time) -> None:
        """Sets the document registration time."""
        if not isinstance(value, Time):
            raise ValueError("Document time must be a datetime.time.")
        current_document_time: Time = cls.get_document_time()
        if value == current_document_time:
            return None
        document_time_edit = DOCUMENT_TIME_EDIT.GetValuePattern()
        str_document_time: str = value.strftime(_TIME_FORMAT)
        assert document_time_edit.SetValue(str_document_time)
        new_document_time: Time = cls.get_document_time()
        assert new_document_time == value
        return None

    @classmethod
    def get_registry_statuses(cls) -> tuple[str, ...]:
        """Returns the registry statuses."""
        return REGISTRY_STATUS_COMBO_BOX.options

    @staticmethod
    def get_registry_status() -> str:
        """Returns the registry status."""
        return REGISTRY_STATUS_COMBO_BOX.value

    @staticmethod
    def set_registry_status(value: str) -> None:
        """Sets the registry status."""
        REGISTRY_STATUS_COMBO_BOX.value = value
        return None

    @classmethod
    def get_registry_offices(cls) -> tuple[str, ...]:
        """Returns the registry offices."""
        return REGISTRY_OFFICE_COMBO_BOX.options

    @staticmethod
    def get_registry_office() -> str:
        """Returns the registry office."""
        return REGISTRY_OFFICE_COMBO_BOX.value

    @staticmethod
    def set_registry_office(value: str) -> None:
        """Sets the registry office."""
        REGISTRY_OFFICE_COMBO_BOX.value = value
        return None

    @classmethod
    def get_registry_areas(cls) -> tuple[str, ...]:
        """Returns the registry areas."""
        return REGISTRY_AREA_COMBO_BOX.options

    @staticmethod
    def get_registry_area() -> str:
        """Returns the registry area."""
        return REGISTRY_AREA_COMBO_BOX.value

    @staticmethod
    def set_registry_area(value: str) -> None:
        """Sets the registry area."""
        REGISTRY_AREA_COMBO_BOX.value = value
        return None

    @classmethod
    def get_payment_statuses(cls) -> tuple[str, ...]:
        """Returns the payment statuses."""
        return PAYMENT_STATUS_COMBO_BOX.options

    @staticmethod
    def get_payment_status() -> str:
        """Returns the payment status."""
        return PAYMENT_STATUS_COMBO_BOX.value

    @staticmethod
    def set_payment_status(value: str) -> None:
        """Sets the payment status."""
        PAYMENT_STATUS_COMBO_BOX.value = value
        return None

    @staticmethod
    def get_title_number() -> int:
        """Returns the title number."""
        title_number_edit = TITLE_NUMBER_EDIT.GetValuePattern()
        str_value: str = title_number_edit.Value
        return int(str_value)

    @staticmethod
    def set_title_number(value: int) -> None:
        """Sets the title number."""
        title_number_edit = TITLE_NUMBER_EDIT.GetValuePattern()
        str_value: str = str(value)
        assert title_number_edit.SetValue(str_value)
        new_value: int = PublicRecordsWindow.get_title_number()
        assert new_value == value
        return None

    @staticmethod
    def get_registry_file_number() -> int:
        """Returns the registry file number."""
        registry_file_number = REGISTRY_FILE_NUMBER_EDIT.GetValuePattern()
        str_value: str = registry_file_number.Value
        return int(str_value)

    @staticmethod
    def set_registry_file_number(value: int) -> None:
        """Sets the registry file number."""
        registry_file_number = REGISTRY_FILE_NUMBER_EDIT.GetValuePattern()
        str_value: str = str(value)
        assert registry_file_number.SetValue(str_value)
        new_value: int = PublicRecordsWindow.get_registry_file_number()
        assert new_value == value
        return None

    @staticmethod
    def get_registry_record_number() -> int:
        """Returns the registry record number."""
        registry_record_number = REGISTRY_RECORD_NUMBER_EDIT.GetValuePattern()
        str_value: str = registry_record_number.Value
        return int(str_value)

    @staticmethod
    def set_registry_record_number(value: int) -> None:
        """Sets the registry record number."""
        registry_record_number = REGISTRY_RECORD_NUMBER_EDIT.GetValuePattern()
        str_value: str = str(value)
        assert registry_record_number.SetValue(str_value)
        new_value: int = PublicRecordsWindow.get_registry_record_number()
        assert new_value == value
        return None

    @staticmethod
    def get_deadline_date() -> Date:
        """Returns the deadline date."""
        deadline_date_edit = DEADLINE_DATE_EDIT.GetValuePattern()
        str_value: str = deadline_date_edit.Value
        datetime: Datetime = Datetime.strptime(str_value, _DATE_FORMAT)
        return datetime.date()

    @staticmethod
    def set_deadline_date(value: Date) -> None:
        """Sets the deadline date."""
        deadline_date_edit = DEADLINE_DATE_EDIT.GetValuePattern()
        str_value: str = value.strftime(_DATE_FORMAT)
        assert deadline_date_edit.SetValue(str_value)
        new_value: Date = PublicRecordsWindow.get_deadline_date()
        assert new_value == value
        return None

    @staticmethod
    def get_tive() -> int:
        """Returns the T.I.V.E."""
        tive_edit = TIVE_EDIT.GetValuePattern()
        str_value: str = tive_edit.Value
        return int(str_value)

    @staticmethod
    def set_tive(value: int) -> None:
        """Sets the tive."""
        tive_edit = TIVE_EDIT.GetValuePattern()
        str_value: str = str(value)
        assert tive_edit.SetValue(str_value)
        new_value: int = PublicRecordsWindow.get_tive()
        assert new_value == value
        return None

    @staticmethod
    def get_total() -> Decimal:
        """Returns the total amount in PEN."""
        total_edit = TOTAL_EDIT.GetValuePattern()
        str_value: str = total_edit.Value
        return Decimal(str_value)

    @staticmethod
    def set_total(value: Decimal) -> None:
        """Sets the total amount in PEN."""
        total_edit = TOTAL_EDIT.GetValuePattern()
        str_value: str = str(value)
        assert total_edit.SetValue(str_value)
        new_value: Decimal = PublicRecordsWindow.get_total()
        assert new_value == value
        return None

    @staticmethod
    def get_associated_order_number() -> int:
        """Returns the associated order number."""
        associated_order_number = ASSOCIATED_ORDER_NUMBER_EDIT.GetValuePattern()
        str_value: str = associated_order_number.Value
        return int(str_value)

    @staticmethod
    def set_associated_order_number(value: int) -> None:
        """Sets the associated order number."""
        associated_order_number = ASSOCIATED_ORDER_NUMBER_EDIT.GetValuePattern()
        str_value: str = str(value)
        assert associated_order_number.SetValue(str_value)
        new_value: int = PublicRecordsWindow.get_associated_order_number()
        assert new_value == value
        return None

    # TODO: Make a get fot the payment method

    @staticmethod
    def set_payment_method_check() -> None:
        """Sets the payment method to check."""
        payment_method = PAYMENT_METHOD_CHECK_RADIO_BUTTON.GetSelectionItemPattern()
        assert payment_method.Select()
        return None

    @staticmethod
    def set_payment_method_cash() -> None:
        """Sets the payment method to cash."""
        payment_method = PAYMENT_METHOD_CASH_RADIO_BUTTON.GetSelectionItemPattern()
        assert payment_method.Select()
        return None

    @staticmethod
    def set_payment_method_card() -> None:
        """Sets the payment method to card."""
        payment_method = PAYMENT_METHOD_CARD_RADIO_BUTTON.GetSelectionItemPattern()
        assert payment_method.Select()
        return None

    @classmethod
    def save(cls) -> None:
        """Saves the public record."""
        save_button = SAVE_BUTTON.GetInvokePattern()
        assert save_button.Invoke()
        success_message: str = "Se registró correctamente."
        DIALOG.expect_message(success_message)
        assert not cls.exists()
        return cls._wait_for_update()

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
