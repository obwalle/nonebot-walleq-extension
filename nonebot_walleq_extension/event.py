from nonebot.adapters.onebot.v12 import RequestEvent, NoticeEvent, MessageEvent, PrivateMessageEvent
from typing_extensions import Literal
# from nonebot.typing import overrides # 以后可能会用


class WQGroupTempPrivateMessageEvent(PrivateMessageEvent):
    """群临时消息"""
    sub_type = "group_temp"
    to_me = True

    group_id: str
    """群 ID"""
    user_name: str
    """发送者用户名称/昵称"""
    ...


class WQFriendPokeNotice(NoticeEvent):
    detail_type: Literal["friend_poke"]

    """好友戳一戳通知"""
    user_id: str
    """发送者 ID"""
    receiver_id: str
    """接收者 ID"""


class WQGroupNameUpdateNotice(NoticeEvent):
    """群名称更新通知"""
    detail_type: Literal["group_name_update"]

    group_id: str
    """群 ID"""
    group_name: str
    """群名称"""
    operator_id: str
    """操作者 ID"""


class WQFriendAddRequestEvent(RequestEvent):
    """好友添加请求"""

    detail_type: Literal["new_friend"]
    user_id: str
    user_name: str
    message: str
    request_id: str
    """flag"""


class WQGroupJoinRequestEvent(RequestEvent):
    """新成员加群申请请求"""

    detail_type: Literal["join_group"]
    request_id: str
    user_id: str
    user_name: str
    group_id: str
    group_name: str
    message: str
    suspicious: bool
    invitor_id: str = None
    invitor_name: str = None


class WQGroupinvItedRequestEvent(RequestEvent):
    """被邀请入群请求"""
    detail_type: str
    group_id: str
    group_name: str
    invitor_id: str = None
    invitor_name: str = None


__all__ = [
    "WQGroupTempPrivateMessageEvent",
    "WQFriendPokeNotice",
    "WQGroupNameUpdateNotice",
    "WQFriendAddRequestEvent",
    "WQGroupJoinRequestEvent",
    "WQGroupinvItedRequestEvent",
]
