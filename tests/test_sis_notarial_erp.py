"""Tests for Sis Notarial ERP application."""

from pysisnotarialerp import SisNotarialERP


def test_sis_notarial_erp(executable_file, username, password) -> None:
    sis_notarial_erp: SisNotarialERP = SisNotarialERP(executable_file)
    main_form = sis_notarial_erp.login(username, password)
    main_form.get_kardex_form()
    return None
