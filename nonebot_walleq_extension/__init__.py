from typing import TYPE_CHECKING, List, Type

from nonebot.adapters.onebot.v12 import Bot, Adapter, Event

from .event import *

# 在编写代码的时候会检查为WQ的bot，但运行时还是V12的Bot，这样就实现了只作为编译器提示，不实现任何功能
if TYPE_CHECKING:
    from .bot import Bot as Bot


ADD_MODELS: List[Type[Event]] = []
for model_name in event.__all__:
    model = getattr(event, model_name)
    if not issubclass(model, Event):
        continue
    ADD_MODELS.append(model)

# 引入扩展event
Adapter.add_custom_model(*ADD_MODELS, impl="Walle-Q", platform="qq")
