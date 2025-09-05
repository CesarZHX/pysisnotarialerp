from .....exceptions import SisNotarialErpException
from .....helpers.get_error_messages import get_error_messages
from .controls import PUBLIC_RECORDS_WINDOW


class PublicRecordsException(SisNotarialErpException):
    """Base class for public records exceptions."""


def raise_public_records_error() -> None:
    """Raises the corresponding public records error."""
    if not (messages := get_error_messages(PUBLIC_RECORDS_WINDOW)):
        raise PublicRecordsException
    errors: tuple[PublicRecordsException, ...]
    errors = tuple(_get_public_records_error(m) for m in messages)
    if len(errors) == 1:
        raise errors[0]
    raise ExceptionGroup("Multiple login errors", errors)


def _get_public_records_error(error_message: str) -> PublicRecordsException:
    default: PublicRecordsException = PublicRecordsException(error_message)
    return _PUBLIC_RECORDS_ERRORS.get(error_message, default)


_PUBLIC_RECORDS_ERRORS: dict[str, PublicRecordsException] = {}
