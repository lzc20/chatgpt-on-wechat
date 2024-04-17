from lib import itchat
import schedule
import time
from datetime import datetime, timedelta


def time_send_message(self):
    # 获取好友列表并更新
    friends = itchat.get_friends(update=True)
    # 获取群聊列表
    groups = itchat.get_chatrooms(update=True)

    # 创建一个字典，键是好友的昵称，值是好友的用户名
    friends_map = {}
    groups_map = {}

    for friend in friends:
        # 使用好友的昵称作为键，用户名作为值
        friends_map[friend['NickName']] = friend['UserName']
    # 打印这个映射的字典，以确认它被正确创建
    print(friends_map)
    for group in groups:
        # 使用群的昵称作为键，用户名作为值
        groups_map[group['NickName']] = group['UserName']
        # 打印这个映射的字典，以确认它被正确创建
    print(groups_map)

    # 通过昵称获取对应的用户名
    nickname_to_lookup = '曲奇'  # 替换为实际想要查找的昵称
    username = method_name(self,friends_map, nickname_to_lookup)

    message = '谢秋晴天下第一大美人'
    send_result = itchat.send(message, toUserName=username)
    print('打印发送结果')
    print(send_result)

    # 发送群消息
    to_group_nickname = '中海技术交流群🍉'
    # 假设我们知道目标群聊的UserName
    to_group_name = method_name(self,groups_map, to_group_nickname)
    group_message = '准备开始发送每日新闻'
    itchat.send(group_message, toUserName=to_group_name)

    itchat.run()

#定时发送消息得模块
def send_scheduled_message():
    # 要发送的消息内容
    message = '这是一条每天9点10分发送的消息'

    # 目标用户的UserName
    to_user_name = 'targetUserName'  # 替换为实际用户的UserName

    # 发送消息
    itchat.send(message, toUserName=to_user_name)
    print(f"消息已发送: {message}")



def method_name(self, friends_map, nickname_to_lookup):
        if nickname_to_lookup in friends_map:
            username = friends_map[nickname_to_lookup]
            print(f"昵称 {nickname_to_lookup} 对应的用户名是: {username}")
        else:
            print(f"没有找到昵称为 {nickname_to_lookup} 的用户。")
        return username


def job():
    # 获取当前时间
    now = datetime.now()
    # 设置目标时间
    target_time = now.replace(hour=9, minute=10, second=0)

    # 如果当前时间已经过了目标时间，则安排在第二天
    if now > target_time:
        target_time += timedelta(days=1)

    # 计算距离目标时间还有多少秒
    seconds_left = (target_time - now).total_seconds()

    # 等待直到目标时间
    time.sleep(seconds_left)

    # 执行定时任务
    send_scheduled_message()


# 设置定时任务
schedule.every().day.at("09:10").do(job)

# 运行调度任务
while True:
    schedule.run_pending()
    time.sleep(1)