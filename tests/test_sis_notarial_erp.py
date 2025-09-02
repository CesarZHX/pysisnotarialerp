"""Tests for Sis Notarial ERP application."""

from datetime import date as Date
from datetime import datetime as Datetime
from datetime import timedelta as Timedelta
from random import choice

from pysisnotarialerp import (
    DATE_PANE,
    KARDEX_TYPES,
    NEW_TEXT,
    PUBLIC_RECORDS_WINDOW,
    KardexNumber,
    KardexType,
    SisNotarialERP,
)


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

    if not PUBLIC_RECORDS_WINDOW.Exists(maxSearchSeconds=0):
        NEW_TEXT.Click()

    today = Date.today()
    yerterday = Date.today() - Timedelta(days=1)
    date = choice((today, yerterday))
    date_format = "%d/%m/%Y"
    str_date = date.strftime(date_format)
    stripped_date = str_date.lstrip("0")
    str_current_date = DATE_PANE.Name
    current_date = Datetime.strptime(str_current_date, date_format).date()
    if date != current_date:
        DATE_PANE.SendKeys(stripped_date)
    str_new_date = DATE_PANE.Name
    new_date = Datetime.strptime(str_new_date, date_format).date()
    assert date == new_date

    return None
