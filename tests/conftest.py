"""Test fixtures."""

from os import environ
from pathlib import Path

from dotenv import load_dotenv
from pydantic import SecretStr
from pytest import fixture

load_dotenv()


@fixture(scope="session")
def executable_file() -> Path:
    return Path(environ["SIS_NOTARIAL_ERP_EXECUTABLE_FILE_PATH"])


@fixture(scope="session")
def username() -> str:
    return environ["USERNAME"]


@fixture(scope="session")
def password() -> SecretStr:
    return SecretStr(environ["PASSWORD"])
