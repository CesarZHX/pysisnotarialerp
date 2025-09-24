"""Public Record model module."""

from datetime import date as Date
from datetime import datetime as Datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, PositiveInt, field_validator
from uiautomation import DataItemControl

from ...constants import DATE_FORMAT
from .constants import RegistryArea, RegistryOffice, RegistryStatus


class PublicRecord(BaseModel):
    """Public Record model."""

    model_config = ConfigDict(arbitrary_types_allowed=True, frozen=True)

    title: str = Field(default="1")
    date: Date = Field(default_factory=Date.today)
    status: RegistryStatus
    download_type: str  # TODO: Replace with StrEnum when the source this is available
    amount: Decimal = Field(default=Decimal("0"), ge=0)
    registry_entry: str | None = Field(default=None)
    submitter: str
    registry_office: RegistryOffice
    registry_area: RegistryArea
    seat: str | None
    deadline_date: Date | None = Field(default=None)
    tive: None = Field(default=None)
    edit_button: DataItemControl
    delete_button: DataItemControl
    return_button: DataItemControl
    discharge_date: Date = Field(default_factory=Date.today)

    @field_validator("title")
    def validate_title(cls, value: str) -> str:
        """PositiveInt or yyyy-PositiveInt"""
        parts = map(int, value.split("-", 1))
        if any(number < 1 for number in parts):
            raise ValueError("Value parts must be positive integers.")
        return value

    @field_validator("registry_entry")
    def validate_registry_entry(cls, value: str | None) -> str | None:
        """registry_entry is an alfanumeric string like P12345678."""
        if value is None:
            return value
        if not value.isalnum():
            raise ValueError("Value must be an alphanumeric string.")
        return value

    @property
    def title_number(self) -> PositiveInt:
        return int(self.title.split("-", 1)[1])

    @classmethod
    def from_table(cls, data: dict[str, Any]) -> "PublicRecord":
        partida = data["Partida"]
        if (fecha_plazo := data["Fecha Plazo"]) is None:
            deadline_date = None
        else:
            deadline_date = Datetime.strptime(fecha_plazo, DATE_FORMAT).date()
        asiento = data["Asiento"]
        discharge_datetime = Datetime.strptime(data["Fecha de Descargo"], DATE_FORMAT)
        return cls(
            title=str(data["Titulo"]),
            date=Datetime.strptime(data["Fecha"], DATE_FORMAT).date(),
            status=RegistryStatus(data["Estado"]),
            download_type=data["Tipo de Descarga"],
            amount=Decimal(data["Monto"]),
            registry_entry=partida,
            submitter=data["Presentante"],
            registry_office=RegistryOffice(data["Oficina Reg."]),
            registry_area=RegistryArea(data["Area Registral"]),
            seat=asiento if asiento is None else asiento,
            deadline_date=deadline_date,
            tive=data["Tive"],
            edit_button=data["Edit."],
            delete_button=data["Elim."],
            return_button=data["Dev"],
            discharge_date=discharge_datetime.date(),
        )
