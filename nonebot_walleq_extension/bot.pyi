from nonebot.adapters.onebot.v12 import Bot as BaseBot
from typing import Any, Dict, List, Literal

from nonebot.adapters.onebot.v12 import Message, MessageEvent

from .event import WQFriendAddRequestEvent, WQGroupinvItedRequestEvent, WQGroupJoinRequestEvent


class Bot(BaseBot):
    # 修改 删除 频道
    async def send_message(
        self,
        *,
        detail_type: Literal["private", "group"] | str,
        user_id: str = ...,
        group_id: str = ...,
        guild_id: str = ...,
        channel_id: str = ...,
        message: Message,
        **kwargs: Any,
    ) -> Dict[Literal["message_id", "time"] | str, Any]:
        """发送消息

        参数:
            detail_type:    发送的类型，可以为 private、group 或扩展的类型，和消息事件的 detail_type 字段对应
            user_id:        用户 ID,当 detail_type 为 private 时必须传入
            group_id:       群 ID,当 detail_type 为 group 时必须传入
            guild_id:       Guild 群组 ID,当 detail_type 为 channel 时必须传入
            channel_id:     频道 ID,当 detail_type 为 channel 时必须传入
            message:        消息内容
            kwargs:         扩展字段
        """
        ...

    # 新增 get_message
    async def get_message(self, *, message_id: str, **kwargs: Any) -> MessageEvent:
        """获取消息

        参数:
            message_id: 唯一的消息 ID
        """
        ...

    #  新增 set_new_friend
    async def set_new_friend(self, user_id: str, request_id: int, accept: bool, **kwargs: Any):
        """处理好友请求

        参数:
            user_id:    用户 ID
            request_id: 请求 ID
            accept:     是否接受请求
            kwargs:     扩展字段
        """
        ...

    # 新增 delete_friend
    async def delete_friend(self, user_id: str, **kwargs: Any):
        """删除好友

        参数:
            user_id:    用户 ID
            kwargs:     扩展字段
        """
        ...

    # 新增 get_new_friend_requests
    async def get_new_friend_requests(self, **kwargs: Any) -> List[WQFriendAddRequestEvent]:
        """获取好友请求列表
        参数:
            kwargs: 扩展字段
        """
        ...

    # 修改 增加禁言事件，默认60秒
    async def ban_group_member(
        self, *, group_id: str, user_id: str, duration: int = 60, **kwargs: Any
    ) -> None:
        """禁言群成员

        参数:
            group_id:   群 ID
            user_id:    用户 ID
            duration:   时长，单位：秒, 默认 60 秒
            kwargs:     扩展字段
        """
        ...

    # 新增 get_join_group_requests
    async def get_join_group_requests(self, **kwargs: Any) -> List[WQGroupJoinRequestEvent]:
        """获取加群申请

        参数:
            kwargs: 扩展字段
        """
        ...

    # 新增 set_join_group
    async def set_join_group(
            self,
            request_id: int,
            user_id: str,
            group_id: str,
            accept: bool,
            block: bool = False,
            message: str = None,
            **kwargs: Any):
        """处理加群请求

        参数:
            request_id:     请求 ID
            user_id:        用户 ID
            group_id:       群 ID
            accept:         是否接受
            block:          是否禁止再次申请
            message:        拒绝理由
            kwargs:         扩展字段
        """
        ...

    # 新增 get_group_inviteds
    async def get_group_inviteds(self, **kwargs: Any) -> List[WQGroupinvItedRequestEvent]:
        """获取群邀请

        参数:
            kwargs: 扩展字段
        """
        ...

    # 新增 set_group_invited
    async def set_group_invited(
            self,
            request_id: int,
            group_id: str,
            accept: bool,
            **kwargs: Any):
        """处理群邀请

        参数:
            request_id:     请求 ID
            group_id:       群 ID
            accept:         是否接受
            kwargs:         扩展字段
        """
        ...

    # TODO: 频道全部没写呢

    # async def get_guild_info(
    #     self, *, guild_id: str, **kwargs: Any
    # ) -> Dict[Literal["guild_id", "guild_name"] | str, str]:
    #     """获取 Guild 信息

    #     参数:
    #         guild_id: 群组 ID
    #         kwargs: 扩展字段
    #     """
    #     ...

    # async def get_guild_list(
    #     self,
    #     **kwargs: Any,
    # ) -> List[Dict[Literal["guild_id", "guild_name"] | str, str]]:
    #     """获取群组列表

    #     参数:
    #         kwargs: 扩展字段
    #     """
    #     ...

    # async def get_channel_info(
    #     self, *, guild_id: str, channel_id: str, **kwargs: Any
    # ) -> Dict[Literal["channel_id", "channel_name"] | str, str]:
    #     """获取频道信息

    #     参数:
    #         guild_id: 群组 ID
    #         channel_id: 频道 ID
    #         kwargs: 扩展字段
    #     """
    #     ...

    # async def get_channel_list(
    #     self, *, guild_id: str, **kwargs: Any
    # ) -> List[Dict[Literal["channel_id", "channel_name"] | str, str]]:
    #     """获取频道列表

    #     参数:
    #         guild_id: 群组 ID
    #         kwargs: 扩展字段
    #     """
    #     ...

    # async def get_guild_member_info(
    #     self, *, guild_id: str, user_id: str, **kwargs: Any
    # ) -> Dict[Literal["user_id", "nickname"] | str, str]:
    #     """获取群组成员信息

    #     参数:
    #         guild_id: 群组 ID
    #         user_id: 用户 ID
    #         kwargs: 扩展字段
    #     """
    #     ...

    # async def get_guild_member_list(
    #     self, *, guild_id: str, **kwargs: Any
    # ) -> List[Dict[Literal["user_id", "nickname"] | str, str]]:
    #     """获取群组成员列表

    #     参数:
    #         guild_id: 群组 ID
    #         kwargs: 扩展字段
    #     """
    #     ...

    # async def set_guild_name(
    #     self, *, guild_id: str, guild_name: str, **kwargs: Any
    # ) -> None:
    #     """设置群组名称

    #     参数:
    #         guild_id: 群组 ID
    #         guild_name: 群组名称
    #         kwargs: 扩展字段
    #     """
    #     ...

    # async def set_channel_name(
    #     self, *, guild_id: str, channel_id: str, channel_name: str, **kwargs: Any
    # ) -> None:
    #     """设置频道名称

    #     参数:
    #         guild_id: 群组 ID
    #         channel_id: 频道 ID
    #         channel_name: 频道名称
    #         kwargs: 扩展字段
    #     """
    #     ...

    # async def leave_guild(self, *, guild_id: str, **kwargs: Any) -> None:
    #     """退出群组

    #     参数:
    #         guild_id: 群组 ID
    #         kwargs: 扩展字段
    #     """
    #     ...
