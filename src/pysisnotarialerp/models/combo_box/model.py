from pydantic import BaseModel, ConfigDict, Field
from uiautomation import ButtonControl, ComboBoxControl, ListControl, ListItemControl

from .exceptions import NoOptionsError, OptionNotExistsError


class ComboBox(BaseModel):

    model_config = ConfigDict(arbitrary_types_allowed=True)

    combo_box: ComboBoxControl = Field(..., frozen=True)
    button: ButtonControl = Field(..., frozen=True)
    list: ListControl = Field(..., frozen=True)

    def __init__(self, combo_box: ComboBoxControl):
        """Initializes a new instance of the SelectInput class."""
        button: ButtonControl = combo_box.ButtonControl(searchDepth=1, Name="Abrir")
        list: ListControl = combo_box.ListControl(searchDepth=1, ClassName="ComboLBox")
        return super().__init__(_combo_box=combo_box, _button=button, _list=list)

    @property
    def value(self) -> str:
        """Returns the value."""
        combo_box: ComboBoxControl = self.combo_box
        type_combo_box = combo_box.GetValuePattern()
        return type_combo_box.Value

    @value.setter
    def value(self, value: str) -> None:
        """Sets the value."""
        option: str = str(value)
        current_value: str = self.value
        if option == current_value:
            return None
        if not (options := self.options):
            raise NoOptionsError
        if option not in options:
            raise OptionNotExistsError(option, options)
        self._collapse()
        combo_box: ComboBoxControl = self.combo_box
        assert combo_box.Select(option)
        new_value: str = self.value
        assert new_value == value
        return None

    @property
    def options(self) -> tuple[str, ...]:
        """Return the options. Each option is unique."""
        options: tuple[str, ...] = tuple(item.Name for item in self.list_items)
        assert len(options) == len(frozenset(options))
        return options

    @property
    def list_items(self) -> tuple[ListItemControl, ...]:
        """Return the list items."""
        list: ListControl = self.list
        self._expand()
        children = tuple(list.GetChildren())
        list_items: tuple[ListItemControl, ...]
        list_items = tuple(c for c in children if isinstance(c, ListItemControl))
        assert len(children) == len(list_items)
        return list_items

    def _expand(self) -> None:
        """Expand the combo box list."""
        if self._is_expanded():
            return None
        return self._toggle()

    def _collapse(self) -> None:
        """Collapse the combo box list."""
        if self._is_expanded():
            return self._toggle()
        return None

    def _is_expanded(self) -> bool:
        """Return True if the combo box list is expanded, False otherwise."""
        list: ListControl = self.list
        return list.Exists(maxSearchSeconds=0)

    def _toggle(self) -> None:
        """Toggle the combo box between expanded and collapsed."""
        button: ButtonControl = self.button
        invoke_pattern = button.GetInvokePattern()
        assert invoke_pattern.Invoke()
        return None
