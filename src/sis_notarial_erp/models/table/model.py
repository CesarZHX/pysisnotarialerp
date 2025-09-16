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
    _horizontal_scroll: ScrollBarControl  # NOTE: Only exists when too many cols.
    _vertical_scroll: ScrollBarControl  # NOTE: Only exists when too many rows.

    def __init__(self, table_control: TableControl) -> None:
        if not isinstance(table_control, TableControl):
            raise ValueError("table_control must be an instance of TableControl.")
        self._table_control: TableControl = table_control
        self._horizontal_scroll = self._get_scroll_bar(Alignment.HORIZONTAL)
        self._vertical_scroll = self._get_scroll_bar(Alignment.VERTICAL)
        self._header_row: CustomControl = table_control.CustomControl(
            searchDepth=1, Name="Fila superior"
        )
        return None

    def read(self) -> tuple[dict[str, DataItemControl | str | None], ...]:
        """Return the table data."""
        return tuple(dict(zip(self._get_headers(), row)) for row in self._get_data())

    def _get_data(self) -> tuple[tuple[DataItemControl | str | None, ...], ...]:
        """Return all table data as tuples of parsed row values."""
        return tuple(self._get_data_row_values(row) for row in self._get_data_rows())

    def _get_data_row_values(
        self, row: CustomControl
    ) -> tuple[DataItemControl | str | None, ...]:
        """Return the row values."""
        cells: tuple[DataItemControl, ...] = self._get_data_cells(row)
        return tuple(self._get_data_cell_value(cell) for cell in cells)

    def _get_headers(self) -> tuple[str, ...]:
        """Return the headers."""
        children: tuple[Control, ...] = tuple(self._header_row.GetChildren())
        cells = tuple(c for c in children if isinstance(c, HeaderControl))
        assert len(children) == len(cells)
        return tuple(c.Name for c in cells)

    def _get_data_cell_value(
        self, cell: DataItemControl
    ) -> DataItemControl | str | None:
        """Return the cell value.
        - Returns ``None`` if the cell is empty.
        - Returns a ``DataItemControl`` if the cell contains a clickable control.
        - Returns a ``str`` otherwise.
        """
        value: str = cell.GetValuePattern().Value
        if value == "(null)":
            return None
        elif value == "System.Drawing.Bitmap":
            return cell
        return value

    def _get_data_cells(self, data_row: CustomControl) -> tuple[DataItemControl, ...]:
        """Return the data cell controls."""
        if not isinstance(data_row, CustomControl):
            raise ValueError("Custom control must be an instance of CustomControl.")
        children: tuple[Control, ...] = tuple(data_row.GetChildren())
        cells = tuple(c for c in children if isinstance(c, DataItemControl))
        assert len(children) == len(cells)
        return cells

    def _get_data_rows(self) -> tuple[CustomControl, ...]:
        """Return the data row controls."""
        controls: tuple[CustomControl, ...] = self._get_rows()
        rows = tuple(c for c in controls if self._row_pattern.match(c.Name))
        assert len(controls) == len(rows + (self._header_row,))
        return rows

    def _get_rows(self) -> tuple[CustomControl, ...]:
        """Return the row controls."""
        children: tuple[Control, ...] = self._get_children()
        custom = tuple(c for c in children if isinstance(c, CustomControl))
        scrolls = tuple(c for c in children if isinstance(c, ScrollBarControl))
        assert 0 < len(scrolls) < 3
        assert len(children) == len(custom) + len(scrolls)
        return custom

    def _get_children(self) -> tuple[Control, ...]:
        """Return the children."""
        table_control: TableControl = self._table_control
        return tuple(table_control.GetChildren())

    def _get_scroll_bar(self, alignment: Alignment) -> ScrollBarControl:
        """Return the scroll bar control."""
        name: str = f"Barra de desplazamiento {alignment}"
        return self._table_control.ScrollBarControl(searchDepth=1, Name=name)
