from uiautomation import WindowControl


def get_error_messages(window: WindowControl) -> tuple[str, ...]:
    """Return the error messages of the SIS Notarial ERP application."""
    error_messages: list[str] = list()
    while error_message := _get_error_message(window):
        error_messages.append(error_message)
    return tuple(error_messages)


def _get_error_message(parent_window: WindowControl) -> str | None:
    """Return the error message of the SIS Notarial ERP application."""
    window = parent_window.WindowControl(searchDepth=1, LocalizedControlType="diálogo")
    text_control = window.TextControl(searchDepth=1, ClassName="Static")
    accept_button = window.ButtonControl(searchDepth=1, Name="Aceptar")
    for control in (text_control, accept_button):
        if not control.Exists(maxSearchSeconds=0):
            return None
    invoke_pattern = accept_button.GetInvokePattern()
    assert invoke_pattern.Invoke()
    return text_control.Name
