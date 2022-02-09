import asyncio
from typing import Any, Callable, Coroutine, Optional, TypeVar

from discord.state import ConnectionState

CoroT = TypeVar("CoroT", bound=Callable[..., Coroutine[Any, Any, Any]])
T = TypeVar("T")
Coro = Coroutine[Any, Any, T]
CoroFunc = Callable[..., Coro[Any]]

class Dispatcher:
    state: Any
    def __init__(self, state: ConnectionState) -> None: ...
    async def run(
        self,
        coro: Callable[..., Coroutine[Any, Any, Any]],
        name: str,
        *args: Any,
        **kwargs: Any
    ) -> None: ...
    def scheduler(
        self,
        coro: Callable[..., Coroutine[Any, Any, Any]],
        name: str,
        *args: Any,
        **kwargs: Any
    ) -> asyncio.Task: ...
    def dispatch(self, name: str, *args, **kwargs) -> None: ...
    def listen(self, coro: Coro) -> Coro: ...
    def add_listener(self, func: CoroFunc, name: Optional[str] = ...): ...
    def remove_listener(self, func: CoroFunc, name: Optional[str] = ...): ...
