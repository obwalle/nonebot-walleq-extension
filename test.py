import datetime

from nonebot.adapters.onebot.v12 import *
from typing_extensions import Literal

from nonebot_walleq_extension import WQFriendAddRequestEvent as test_event
from nonebot_walleq_extension import *

# 引入测试event
# Adapter.add_custom_model((test_event),
#                          impl="Walle-Q",
#                          platform="qq"
#                          )

# 构建测试数据
test_data = {
    'id': '00000000-0000-0000-16f7-e2701484e534',
    'impl': 'Walle-Q', 'platform': 'qq',
    'self_id': '123456789',
    'time': 1655036480.0,
    'type': 'request',
    'detail_type': 'new_friend',
    'sub_type': '',
    'request_id': 1653473791000000,
    'user_id': '987654321',
    'user_name': 'Sclock',
    'message': ''
}

# 测试能否实例化
event = Adapter.json_to_event(test_data, "test_id")
match event:
    case test_event():
        print("WQFriendAddRequestEvent")
        ...
    case RequestEvent():
        print("RequestEvent")
        ...
    case Event():
        print("实例化失败")
    case _:
        print("数据错误")
