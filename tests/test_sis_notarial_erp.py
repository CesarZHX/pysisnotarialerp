"""Tests for Sis Notarial ERP window."""

from time import sleep

from pytest import skip

from pysisnotarialerp.sis_notarial_erp import KARDEX_BUTTON, WINDOW

if not WINDOW.Exists():
    skip("Window not found.", allow_module_level=True)


def test_window_states_and_lifecycle() -> None:
    """
    Verifies the window can:
      - Be set to 'always on top' (topmost)
      - Be activated
      - Be minimized and restored
      - Be maximized and restored
    """
    WINDOW.SetTopmost(True)
    WINDOW.SetActive()
    WINDOW.Minimize()
    WINDOW.Restore()
    WINDOW.Minimize()
    WINDOW.Maximize()
    WINDOW.Restore()
    return sleep(1)


def test_click_kardex_button() -> None:
    """Verifies the kardex button is clickable."""
    KARDEX_BUTTON.Click()
    return sleep(1)
