from typing import Sequence

from ...exceptions import SisNotarialErpException


class ComboBoxException(SisNotarialErpException):
    """Base class for combo box exceptions."""


class NoOptionsError(ComboBoxException):
    """Raised when there are no options."""


class OptionNotExistsError(ComboBoxException):
    """Raised when the option does not exist."""

    def __init__(self, unexisting_option: str, available_options: Sequence[str]):
        """Initializes a new instance of the OptionNotExistsError class."""
        if not unexisting_option:
            raise NoOptionsError
        self.unexisting_option: str = unexisting_option
        self.available_options: Sequence[str] = available_options
        first_message: str = f"Option '{unexisting_option}' not exists."
        last_message: str = f"Available options: {', '.join(available_options)}."
        super().__init__(first_message + last_message)
