from typing import Any, Callable, Coroutine, List, Optional

from discord.types.dict import Dict

from ..state import ConnectionState

class ApplicationCommandRegistry:
    factory: Any
    state: Any
    dispatcher: Any
    unregistered_commands: Any
    def __init__(self, rest_factory, state: ConnectionState) -> None: ...
    async def run(
        self, coro: Callable[..., Coroutine[Any, Any, Any]], data, state
    ) -> None: ...
    async def on_ready(self) -> None: ...
    async def check_application_commands(self, rglobal) -> None: ...
    async def register_guild_slash_command(
        self,
        guild_id,
        name,
        description,
        callback,
        options: Optional[List[Dict]] = ...,
        default_permission: bool = ...,
    ) -> dict: ...
    async def register_global_slash_command(
        self,
        name,
        description,
        callback,
        options: Optional[List[Dict]] = ...,
        default_permission: bool = ...,
    ) -> dict: ...
