import datetime
from typing import Any, Optional, Union

from discord.color import Color
from discord.colour import Colour

class Embed:
    obj: Any
    def __init__(
        self,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        url: Optional[str] = ...,
        date: Optional[str] = ...,
        color: Optional[Union[int, Color]] = ...,
        colour: Optional[Union[int, Colour]] = ...,
        timestamp: datetime.datetime = ...,
    ) -> None: ...
    def to_dict(self): ...
    def set_footer(self, text: str = ..., icon_url: str = ...): ...
    def remove_footer(self) -> None: ...
    def set_thumbnail(self, url: str = ...): ...
    def set_author(self, name: str, url: str = ..., icon_url: str = ...): ...
    def remove_author(self) -> None: ...
    def add_field(self, name: str, value: str, inline: bool = ...): ...
    def remove_field(self, name: str): ...
