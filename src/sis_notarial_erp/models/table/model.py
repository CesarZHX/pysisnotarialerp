"""Table model module."""

from re import Pattern, compile

from uiautomation import (
    Control,
    CustomControl,
    DataItemControl,
    HeaderControl,
    ScrollBarControl,
    TableControl,
)

from .constants import Alignment


class Table:
    """Table model class."""

    _row_pattern: Pattern = compile(r"^Fila (0|[1-9]\d*)$")
    _max_visible_rows: int = 7

    _horizontal_scroll: ScrollBarControl

    def __init__(self, table_control: TableControl) -> None:
        if not isinstance(table_control, TableControl):
            raise ValueError("table_control must be an instance of TableControl.")
        self._table_control: TableControl = table_control
        self._horizontal_scroll = self._get_scroll_bar_control(Alignment.HORIZONTAL)
        self._vertical_scroll = self._get_scroll_bar_control(Alignment.VERTICAL)
        self._header_row: CustomControl = table_control.CustomControl(
            searchDepth=1, Name="Fila superior"
        )
        assert self._max_visible_rows >= 0
        return None

    def _get_headers(self) -> tuple[str, ...]:
        """Return the headers."""
        return tuple(c.Name for c in self._get_header_controls())

    def _get_header_controls(self) -> tuple[HeaderControl, ...]:
        """Return the header controls."""
        children: tuple[Control, ...] = tuple(self._header_row.GetChildren())
        headers = tuple(c for c in children if isinstance(c, HeaderControl))
        assert len(children) == len(headers)
        return headers

    def _get_row_data_item_controls(self) -> tuple[tuple[DataItemControl, ...], ...]:
        """Return the data item controls."""
        rows: tuple[CustomControl, ...] = self._get_row_custom_controls()
        return tuple(map(self._get_data_item_controls, rows))

    def _get_data_item_controls(
        self, custom_control: CustomControl
    ) -> tuple[DataItemControl, ...]:
        """Return the data item controls."""
        if not isinstance(custom_control, CustomControl):
            raise ValueError("Custom control must be an instance of CustomControl.")
        children: tuple[Control, ...] = tuple(custom_control.GetChildren())
        data_items = tuple(c for c in children if isinstance(c, DataItemControl))
        assert len(children) == len(data_items)
        return data_items

    def _get_row_custom_controls(self) -> tuple[CustomControl, ...]:
        """Return the row custom controls."""
        controls: tuple[CustomControl, ...] = self._get_custom_controls()
        rows = tuple(c for c in controls if self._row_pattern.match(c.Name))
        assert len(controls) == len(rows + (self._header_row,))
        return rows

    def _get_custom_controls(self) -> tuple[CustomControl, ...]:
        """Return the custom controls."""
        children: tuple[Control, ...] = self._get_controls()
        custom = tuple(c for c in children if isinstance(c, CustomControl))
        assert len(children) == len(custom)
        return custom

    def _get_controls(self) -> tuple[Control, ...]:
        """Return the table controls."""
        table_control: TableControl = self._table_control
        return tuple(table_control.GetChildren())

    def _get_scroll_bar_control(self, alignment: Alignment) -> ScrollBarControl:
        """Return the scroll bar control."""
        name: str = f"Barra de desplazamiento {alignment}"
        return self._table_control.ScrollBarControl(searchDepth=1, Name=name)

    def _has_vertical_scroll_bar(self) -> bool:
        """Return True if the table has a vertical scroll bar, False otherwise."""
        return len(self._get_row_custom_controls()) > self._max_visible_rows

    def _get_vertical_scroll_bar_control(self) -> ScrollBarControl | None:
        """Returns the vertical scroll bar control if it should exist, None otherwise."""
        if not self._has_vertical_scroll_bar():
            return None
        return self._get_scroll_bar_control(Alignment.VERTICAL)
