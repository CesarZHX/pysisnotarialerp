"""Tests for Sis Notarial ERP application."""

from datetime import date as Date
from datetime import timedelta as Timedelta
from random import choice

from sis_notarial_erp import KARDEX_TYPES, KardexNumber, KardexType, LoginWindow


def test_sis_notarial_erp(executable_file, username, password) -> None:
    """Tests the Sis Notarial ERP application."""
    login_window: LoginWindow = LoginWindow(executable_file)
    # TODO: Wait up to 2 simultaneuos error in login (data too long is the one expected to be the first of two errors), the rest, wait just for one.
    main_window = login_window.login(username, password)
    kardex_window = main_window.get_kardex_window()

    old_kardex_type: KardexType = kardex_window.get_kardex_type()
    kardex_type: KardexType = choice(tuple(KARDEX_TYPES))
    kardex_window.set_kardex_type(kardex_type)
    new_kardex_type: KardexType = kardex_window.get_kardex_type()
    assert new_kardex_type == kardex_type

    assert (old_kardex_number := kardex_window.get_kardex_number())
    assert (_kardex_number := kardex_window.get_kardex_number())
    kardex_number: KardexNumber = KardexNumber(_kardex_number.root - 1)
    kardex_window.set_kardex_number(kardex_number)
    assert (new_kardex_number := kardex_window.get_kardex_number())
    assert new_kardex_number == kardex_number

    public_records_window = kardex_window.get_public_records_window()

    today = Date.today()
    yerterday = Date.today() - Timedelta(days=1)
    date = choice((today, yerterday))
    public_records_window.set_document_date(date)

    return None
