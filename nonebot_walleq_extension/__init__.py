from typing import List, Type

from nonebot.adapters.onebot.v12 import Adapter, Event

from .event import *


ADD_MODELS: List[Type[Event]] = []
for model_name in event.__all__:
    model = getattr(event, model_name)
    if not issubclass(model, Event):
        continue
    ADD_MODELS.append(model)

# 引入扩展event
Adapter.add_custom_model(*ADD_MODELS, impl="Walle-Q", platform="qq")
