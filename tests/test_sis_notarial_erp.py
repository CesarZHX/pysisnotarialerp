"""Tests for Sis Notarial ERP application."""

from subprocess import Popen

from pysisnotarialerp import KARDEX_BUTTON, WINDOW, login


def test_sis_notarial_erp(executable_file, username, password) -> None:
    Popen(executable_file)
    login(username, password)
    WINDOW.SetTopmost(True)
    return KARDEX_BUTTON.Click()
