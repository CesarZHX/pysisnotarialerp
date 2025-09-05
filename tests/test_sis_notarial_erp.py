"""Tests for Sis Notarial ERP application."""

from datetime import date as Date
from datetime import timedelta as Timedelta
from random import choice

from pysisnotarialerp import KARDEX_TYPES, KardexNumber, KardexType, SisNotarialERP


def test_sis_notarial_erp(executable_file, username, password) -> None:
    """Tests the Sis Notarial ERP application."""
    sis_notarial_erp: SisNotarialERP = SisNotarialERP(executable_file)
    main_form = sis_notarial_erp.login(username, password)
    kardex_form = main_form.get_kardex_window()

    old_kardex_type: KardexType = kardex_form.get_kardex_type()
    kardex_type: KardexType = choice(tuple(KARDEX_TYPES))
    kardex_form.set_kardex_type(kardex_type)
    new_kardex_type: KardexType = kardex_form.get_kardex_type()
    assert new_kardex_type == kardex_type

    assert (old_kardex_number := kardex_form.get_kardex_number())
    assert (_kardex_number := kardex_form.get_kardex_number())
    kardex_number: KardexNumber = KardexNumber(_kardex_number.root - 1)
    kardex_form.set_kardex_number(kardex_number)
    assert (new_kardex_number := kardex_form.get_kardex_number())
    assert new_kardex_number == kardex_number

    public_records_window = kardex_form.get_public_records_window()

    today = Date.today()
    yerterday = Date.today() - Timedelta(days=1)
    date = choice((today, yerterday))
    public_records_window.set_document_date(date)

    return None
