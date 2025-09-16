"""Public Record model module."""

from datetime import date as Date
from datetime import datetime as Datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, PositiveInt
from uiautomation import DataItemControl

from ...constants import DATE_FORMAT
from .constants import RegistryArea, RegistryOffice, RegistryStatus


class PublicRecord(BaseModel):
    """Public Record model."""

    model_config = ConfigDict(arbitrary_types_allowed=True, frozen=True)

    title: PositiveInt = Field(default=1)
    date: Date = Field(default_factory=Date.today)
    status: RegistryStatus
    download_type: str  # TODO: Replace with StrEnum when the source this is available
    amount: Decimal = Field(default=Decimal("0"), ge=0)
    registry_entry: PositiveInt | None = Field(default=None)
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
            title=int(data["Titulo"]),
            date=Datetime.strptime(data["Fecha"], DATE_FORMAT).date(),
            status=RegistryStatus(data["Estatus"]),
            download_type=data["Tipo de Descarga"],
            amount=Decimal(data["Monto"]),
            registry_entry=partida if partida is None else int(partida),
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
