<div align="center">

# NoneBot-Adapter-OneBot-walle-q

_✨ 基于 OneBot 协议的 walle_q 扩展适配 ✨_

</div>

# 已支持的扩展事件

# 事件 Event

所有事件共有字段

| 字段     | 类型   | 说明                 |
| -------- | ------ | -------------------- |
| id       | String | 事件 ID              |
| impl     | String | 实现名，即 `Walle-Q` |
| platform | String | 平台名，即 `qq`      |
| self_id  | String | Bot ID               |
| time     | f64    | 事件戳，单位：秒     |

## 消息事件 message

### [扩展]群临时消息 message.private.group_temp

| 字段        | 类型    | 说明            |
| ----------- | ------- | --------------- |
| message_id  | String  | 消息 ID         |
| message     | Message | 消息对象        |
| alt_message | String  | 消息文本        |
| user_id     | String  | 发送者 ID       |
| group_id    | String  | 群 ID           |
| user_name   | String  | 发送者 nickname |

## 通知事件 notice

### [扩展]好友戳一戳 notice.friend_poke

| 字段        | 类型   | 说明      |
| ----------- | ------ | --------- |
| user_id     | String | 发送者 ID |
| receiver_id | String | 接收者 ID |

### [扩展]群名称更新 notice.group_name_update

| 字段        | 类型   | 说明      |
| ----------- | ------ | --------- |
| group_id    | String | 群 ID     |
| group_name  | String | 群名称    |
| operator_id | String | 操作者 ID |

## 请求事件 request

### [扩展]好友添加请求 request.new_friend

| 字段       | 类型   | 说明          |
| ---------- | ------ | ------------- |
| request_id | i64    | 请求 ID       |
| user_id    | String | 用户 ID       |
| user_name  | String | 用户名称/昵称 |
| message    | String | 请求信息      |

### [扩展]新成员加群申请 request.join_group

| 字段         | 类型             | 说明          |
| ------------ | ---------------- | ------------- |
| request_id   | i64              | 请求 ID       |
| user_id      | String           | 用户 ID       |
| user_name    | String           | 用户名称/昵称 |
| group_id     | String           | 群 ID         |
| group_name   | String           | 群名称        |
| message      | String           | 请求信息      |
| suspicious   | bool             | 是否可疑      |
| invitor_id   | Option\<String\> | 邀请人 ID     |
| invitor_name | Option\<String\> | 邀请人名称    |

### [扩展]群邀请 request.group_invited

| 字段         | 类型             | 说明       |
| ------------ | ---------------- | ---------- |
| request_id   | i64              | 请求 ID    |
| group_id     | String           | 群 ID      |
| group_name   | String           | 群名称     |
| invitor_id   | Option\<String\> | 邀请人 ID  |
| invitor_name | Option\<String\> | 邀请人名称 |
