from nonebot.adapters.onebot.v12 import *

from nonebot_walleq_extension import *
from nonebot_walleq_extension import WQGroupTempMessageEvent as test_event

# 引入测试event
# Adapter.add_custom_model((test_event),
#                          impl="Walle-Q",
#                          platform="qq"
#                          )

# 构建测试数据
test_data = {
    'id': '00000000-0000-0000-16f8-6865f4609ed4',
    'impl': 'Walle-Q',
    'platform': 'qq',
    'self_id': '123456789',
    'time': 1655187651.0,
    'type': 'message',
    'detail_type': 'group_temp',
    'sub_type': '',
    'group_id': '987654321',
    'user_name': '',
    'message_id': '29662',
    'message': [{'type': 'text',
                 'data': {'text': '1'}}],
    'alt_message': '1',
    'user_id': '1342810270'
}

# 测试能否实例化
event = Adapter.json_to_event(test_data,
                              "test_id")

match event:
    case test_event():
        print("WQFriendAddRequestEvent")
        print(event.to_me)
        print(event.is_tome())
        ...
    case MessageEvent():
        print("MessageEvent")
        print(event.to_me)
        print(event.is_tome())
        ...
    case Event():
        print("实例化失败")
    case _:
        print("数据错误")
