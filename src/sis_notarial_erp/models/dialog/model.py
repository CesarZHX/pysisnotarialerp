"""Dialog model module."""

from pydantic import BaseModel, ConfigDict, Field
from uiautomation import ButtonControl, TextControl, WindowControl

from .exceptions import UnexpectedDialogMessageError


class Dialog(BaseModel):
    """Dialog model class."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    parent_window: WindowControl = Field(..., frozen=True)
    window: WindowControl = Field(..., frozen=True)
    text_control: TextControl = Field(..., frozen=True)
    accept_button: ButtonControl = Field(..., frozen=True)

    def __init__(self, parent_window: WindowControl) -> None:
        """Initializes a new instance of the Dialog class."""
        dw = parent_window.WindowControl(searchDepth=1, LocalizedControlType="diálogo")
        return super().__init__(
            parent_window=parent_window,
            window=dw,
            text_control=dw.TextControl(searchDepth=1, ClassName="Static"),
            accept_button=dw.ButtonControl(searchDepth=1, Name="Aceptar"),
        )

    def get_value(self) -> str:
        """Returns the value. This immediately closes the dialog."""
        text_control: TextControl = self.text_control
        text: str = text_control.Name
        self.close()
        return text

    def exists(self) -> bool:
        """Returns True if the dialog exists, False otherwise."""
        window: WindowControl = self.window
        return window.Exists(maxSearchSeconds=0)

    def expect_message(self, expected_message: str) -> None:
        """Waits for the dialog to appear, checks its message and closes it."""
        dialog_message: str = self.get_value()
        if expected_message != dialog_message:
            raise UnexpectedDialogMessageError(dialog_message)
        return None

    def close(self) -> None:
        """Closes the dialog."""
        accept_button: ButtonControl = self.accept_button
        if accept_button.Exists(maxSearchSeconds=0):
            invoke_pattern = accept_button.GetInvokePattern()
            assert invoke_pattern.Invoke()
        return None
