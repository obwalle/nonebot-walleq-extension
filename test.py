import datetime
from typing_extensions import Literal
from nonebot.adapters.onebot.v12 import Adapter, Event, PrivateMessageEvent

from nonebot_walleq_extension import WQGroupTempPrivateMessageEvent as test_event

# 引入测试event
# Adapter.add_custom_model((test_event),
#                          impl="Walle-Q",
#                          platform="qq"
#                          )

# 构建测试数据
test_data = {
    'id': '00000000-0000-0000-16f7-dee8e66251bc',
    'impl': 'Walle-Q',
    'platform': 'qq',
    'self_id': '2657565907',
    'time': 1655036480.0,
    'type': 'message',
    'detail_type': 'private',
    'sub_type': '',
    'user_name': '',
    'message_id': '4561',
    'message': [{'type': 'text', 'data': {'text': '1'}}],
    'alt_message': '1',
    'user_id': '1342810270'
}

# 测试能否实例化
event = Adapter.json_to_event(test_data, "test_id")
match event:
    case test_event():
        print("WQGroupTempPrivateMessageEvent")
        ...
    case PrivateMessageEvent():
        print("PrivateMessageEvent")
        ...
    case Event():
        print("实例化失败")
    case _:
        print("数据错误")
