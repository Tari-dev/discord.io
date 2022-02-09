import datetime
import typing
from typing import Any, Optional

from ..enums import ScheduledEventType
from ..file import File
from ..flags import MessageFlags
from ..snowflake import Snowflakeish
from ..state import ConnectionState
from ..types import allowed_mentions
from ..types.dict import Dict

class RESTFactory:
    proxy: Any
    proxy_auth: Any
    state: Any
    rest: Any
    def __init__(
        self,
        state: typing.Optional[ConnectionState] = ...,
        proxy: typing.Optional[str] = ...,
        proxy_auth: typing.Optional[str] = ...,
    ) -> None: ...
    token: Any
    async def login(
        self, token: str
    ) -> typing.Coroutine[typing.Any, typing.Any, typing.Union[typing.Any, None]]: ...
    def logout(
        self,
    ) -> typing.Coroutine[typing.Any, typing.Any, typing.Union[typing.Any, None]]: ...
    def get_gateway_bot(
        self,
    ) -> typing.Coroutine[typing.Any, typing.Any, typing.Union[typing.Any, None]]: ...
    def create_message(
        self,
        channel: Snowflakeish,
        content: typing.Optional[str] = ...,
        files: typing.Optional[typing.Sequence[File]] = ...,
        tts: typing.Optional[bool] = ...,
        embeds: typing.List[Dict] = ...,
        allowed_mentions: typing.Optional[allowed_mentions.MentionObject] = ...,
        message_reference: typing.Optional[dict] = ...,
        components: typing.Optional[list[Dict]] = ...,
    ) -> typing.Coroutine[typing.Any, typing.Any, typing.Union[typing.Any, None]]: ...
    def get_channel(self, channel: typing.Optional[Snowflakeish] = ...): ...
    def edit_channel(
        self,
        name: typing.Optional[str] = ...,
        channel: typing.Optional[Snowflakeish] = ...,
        type: typing.Optional[str] = ...,
    ): ...
    def create_invite(
        self,
        *,
        channel_id: typing.Optional[Snowflakeish] = ...,
        reason: typing.Optional[str] = ...,
        max_age: typing.Optional[int] = ...,
        max_uses: typing.Optional[int] = ...,
        tempoary: typing.Optional[bool] = ...,
        unique: typing.Optional[bool] = ...
    ): ...
    def create_global_application_command(
        self,
        application_id: Snowflakeish,
        name: str,
        description: str,
        options: typing.Optional[typing.List[Dict]] = ...,
        default_permission: typing.Optional[bool] = ...,
        type: int = ...,
    ): ...
    def get_global_application_command(
        self, application_id: Snowflakeish, command: Snowflakeish
    ): ...
    def edit_global_application_command(
        self,
        application_id: Snowflakeish,
        command_id: Snowflakeish,
        name: str,
        description: str,
        options: typing.Optional[typing.List[Dict]] = ...,
        default_permission: typing.Optional[bool] = ...,
    ): ...
    def get_global_application_commands(self, application_id: Snowflakeish): ...
    def delete_global_application_command(self, application_id: int, command: int): ...
    def create_guild_application_command(
        self,
        application_id: Snowflakeish,
        guild_id: Snowflakeish,
        name: str,
        description: str,
        options: typing.Optional[typing.List[Dict]],
        default_permission: typing.Optional[bool] = ...,
        type: int = ...,
    ): ...
    def get_guild_application_command(
        self,
        application_id: Snowflakeish,
        guild_id: Snowflakeish,
        command: Snowflakeish,
    ): ...
    def get_guild_application_commands(
        self, application_id: Snowflakeish, guild_id: Snowflakeish
    ): ...
    def delete_guild_application_command(
        self, application_id: int, guild_id: int, command: int
    ): ...
    def edit_guild_application_command(
        self,
        application_id: Snowflakeish,
        command_id: Snowflakeish,
        guild_id: Snowflakeish,
        name: str,
        description: str,
        options: typing.Optional[typing.List[Dict]] = ...,
        default_permission: typing.Optional[bool] = ...,
    ): ...
    def create_interaction_response(
        self,
        interaction_id: int,
        interaction_token: str,
        content: str,
        embeds: typing.Optional[typing.List[typing.Dict]] = ...,
        tts: typing.Optional[bool] = ...,
        allowed_mentions: typing.Optional[allowed_mentions.MentionObject] = ...,
        flags: typing.Optional[MessageFlags] = ...,
        components: typing.Optional[dict] = ...,
    ): ...
    def get_initial_response(self, application_id, interaction_token): ...
    def create_followup_message(
        self,
        application_id,
        interaction_token,
        content: str,
        embeds: typing.Optional[typing.List[dict]] = ...,
        allowed_mentions: typing.Optional[allowed_mentions.MentionObject] = ...,
        components: typing.Optional[typing.List[Dict]] = ...,
        flags: typing.Optional[MessageFlags] = ...,
    ): ...
    def get_followup_message(self, application_id, interaction_token, message): ...
    def get_audit_log_entry(
        self,
        guild: Snowflakeish,
        user_id: typing.Optional[Snowflakeish] = ...,
        action_type: typing.Optional[int] = ...,
        before: typing.Optional[Snowflakeish] = ...,
        limit: typing.Optional[int] = ...,
    ): ...
    def get_guild_member(self, guild_id, user): ...
    def get_guild_members(
        self,
        guild_id,
        limit: typing.Optional[int] = ...,
        after: typing.Optional[int] = ...,
    ): ...
    def modify_guild_member(
        self,
        guild_id: int,
        member: int,
        nick: typing.Optional[str] = ...,
        roles: typing.Optional[typing.List[int]] = ...,
        mute: typing.Optional[bool] = ...,
        deaf: typing.Optional[bool] = ...,
        channel_id: typing.Optional[int] = ...,
        timeout: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
    ): ...
    def get_guild(self, guild_id: int): ...
    def modify_guild(
        self,
        guild_id: int,
        reason: Optional[str] = ...,
        name: Optional[str] = ...,
        verification_level: Optional[int] = ...,
        default_message_notifications: Optional[int] = ...,
        explicit_content_filter: Optional[int] = ...,
        afk_channel_id: Optional[int] = ...,
        afk_timeout: Optional[int] = ...,
    ): ...
    def get_user(self, user: int): ...
    def get_scheduled_events(self, guild_id: int): ...
    def create_scheduled_event(
        self,
        guild_id: int,
        name: str,
        start_time: datetime.datetime,
        type: ScheduledEventType,
        end_time: Optional[datetime.datetime] = ...,
        description: Optional[str] = ...,
        privacy_level: Optional[int] = ...,
        channel_id: Optional[int] = ...,
        metadata: Optional[Any] = ...,
        image: Optional[File] = ...,
    ): ...
    def create_guild_sticker(
        self,
        guild_id: int,
        name: str,
        tags: str,
        file: File,
        reason: Optional[str] = ...,
        description: Optional[str] = ...,
    ): ...
    async def ws_connect(self, url: str, *, compress: int = ...) -> Any: ...
