"""Public Record model module."""

from datetime import date as Date
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, PositiveInt
from uiautomation import DataItemControl

from .constants import RegistryArea, RegistryOffice, RegistryStatus


class PublicRecord(BaseModel):
    """Public Record model."""

    model_config = ConfigDict(arbitrary_types_allowed=True, frozen=True)

    title: PositiveInt = Field(default=1)
    date: Date = Field(default_factory=Date.today)
    status: RegistryStatus
    download_type: str  # TODO: Replace with StrEnum
    amount: Decimal = Field(default=Decimal("0"), ge=0)
    registry_entry: PositiveInt | None = Field(default=None)
    submitter: str
    registry_office: RegistryOffice
    registry_area: RegistryArea
    seat: str | None
    deadline_date: Date | None
    tive: None = Field(default=None)
    edit_button: DataItemControl
    delete_button: DataItemControl
    return_button: DataItemControl
    discharge_date: Date = Field(default_factory=Date.today)

    @classmethod
    def from_table(cls, data: dict[str, Any]) -> "PublicRecord":
        partida = data["Partida"]
        fecha_plazo = data["Fecha Plazo"]
        asiento = data["Asiento"]
        return cls(
            title=int(data["Titulo"]),
            date=data["Fecha"],
            status=RegistryStatus(data["Estatus"]),
            download_type=data["Tipo de Descarga"],
            amount=Decimal(data["Monto"]),
            registry_entry=partida if partida is None else int(partida),
            submitter=data["Presentante"],
            registry_office=RegistryOffice(data["Oficina Reg."]),
            registry_area=RegistryArea(data["Area Registral"]),
            seat=asiento if asiento is None else asiento,
            deadline_date=fecha_plazo if fecha_plazo is None else fecha_plazo,
            tive=data["Tive"],
            edit_button=data["Edit."],
            delete_button=data["Elim."],
            return_button=data["Dev"],
            discharge_date=data["Fecha de Descargo"],
        )
