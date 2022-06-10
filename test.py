import datetime
from typing_extensions import Literal
from nonebot.adapters.onebot.v12 import Adapter, Event

from nonebot_walleq_extension import WQFriendAddRequestEvent as test_event

# 引入测试event
# Adapter.add_custom_model((test_event),
#                          impl="Walle-Q",
#                          platform="qq"
#                          )

# 构建测试数据
test_data = {'id': '00000000-0000-0000-16f7-33949fbdc188',
             'impl': 'Walle-Q',
             'platform': 'qq',
             'self_id': '123456789',
             'time': datetime.datetime(2022, 6, 1, 12, 0, 0, 510135, tzinfo=datetime.timezone.utc),
             'type': 'request',
             'detail_type': 'new_friend',
             'sub_type': '',
             'user_name': '测试',
             'request_id': 1652676348000000,
             'message': '测试请求',
             'user_id': '987654321'
             }

# 测试能否实例化
event = Adapter.json_to_event(test_data, "test_id")
match event:
    case test_event():
        print("FriendAddRequestEvent")

        print(event.detail_type)
        print(event.user_id)
        print(event.user_name)
        print(event.message)
        print([event.request_id])
        ...
    case Event():
        print("实例化失败")
    case _:
        print("数据错误")
