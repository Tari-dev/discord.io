from typing import Any, List, Optional, Sequence

from discord.file import File
from discord.types import allowed_mentions

from .embed import Embed
from .user import User

class Message:
    from_dict: Any
    app: Any
    content: Any
    def __init__(self, msg: dict, app) -> None: ...
    @property
    def channel(self): ...
    @property
    def id(self) -> int: ...
    @property
    def guild(self): ...
    @property
    def author(self) -> User: ...
    async def send(
        self,
        content: Optional[str] = ...,
        files: Optional[Sequence[File]] = ...,
        embed: Optional[Embed] = ...,
        embeds: Optional[List[Embed]] = ...,
        tts: Optional[bool] = ...,
        allowed_mentions: Optional[allowed_mentions.MentionObject] = ...,
        components: List[dict[str, Any]] = ...,
        component: Any | None = ...,
    ): ...
    async def reply(
        self,
        content: Optional[str] = ...,
        files: Optional[Sequence[File]] = ...,
        embed: Optional[Embed] = ...,
        embeds: Optional[List[Embed]] = ...,
        tts: Optional[bool] = ...,
        allowed_mentions: Optional[allowed_mentions.MentionObject] = ...,
        components: List[dict[str, Any]] = ...,
        component: dict[str, Any] = ...,
    ): ...
