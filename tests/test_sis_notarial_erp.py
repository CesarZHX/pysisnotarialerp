"""Tests for Sis Notarial ERP application."""

from datetime import date as Date
from decimal import Decimal
from random import choice

from sis_notarial_erp import (
    KARDEX_TYPES,
    PUBLIC_RECORDS_TABLE,
    KardexNumber,
    KardexType,
    LoginWindow,
    PublicRecord,
)


def test_create_kardex(executable_file, username, password) -> None:
    """Tests the kardex creation application."""
    login_window: LoginWindow = LoginWindow(executable_file)
    main_window = login_window.login(username, password)
    kardex_window = main_window.get_kardex_window()

    old_kardex_type: KardexType = kardex_window.get_kardex_type()
    kardex_type: KardexType = choice(tuple(KARDEX_TYPES))
    kardex_window.set_kardex_type(kardex_type)
    new_kardex_type: KardexType = kardex_window.get_kardex_type()
    assert new_kardex_type == kardex_type

    assert (old_kardex_number := kardex_window.get_kardex_number())
    kardex_number: KardexNumber = KardexNumber(old_kardex_number.root - 1)
    kardex_window.set_kardex_number(kardex_number)
    assert (new_kardex_number := kardex_window.get_kardex_number())
    assert new_kardex_number == kardex_number

    kardex_window.go_to_public_records_panel()
    table = PUBLIC_RECORDS_TABLE.read()
    records = tuple(PublicRecord.from_table(row) for row in table)
    dumped_records = tuple(record.model_dump() for record in records)

    # TODO: Make a method for kardex_window to create a new public records directly.
    main_window.unset_topmost()
    public_records_window = kardex_window.get_public_records_window()

    public_records_window.set_document_date(Date.today())
    public_records_window.set_registry_status("PRESENTADO EN LINEA")
    public_records_window.set_registry_office("LIMA")
    public_records_window.set_registry_area("PERSONAS JURIDICAS")
    public_records_window.set_title_number(100000)
    public_records_window.set_payment_status("PAGADO EN LINEA")
    public_records_window.set_total(Decimal("100.00"))
    public_records_window.set_associated_order_number(1010)

    public_records_window.save()  # NOTE or close to do not create the record.
    # NOTE: If you created the record, you can delete delete it later.

    return None
