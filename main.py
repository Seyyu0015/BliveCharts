import asyncio
import datetime

import callback as callback
from bilibili_api import user, live, sync

import photo

"""连接房间获取礼物列表并排行"""

try:
    roomid = open('roomid.txt', 'r')
    roomn = int(roomid.read())
    roomid.close()
    print('roomid:', roomn)

except:
    print('未从roomid.txt中获取信息')
    roomn = input('输入房间号来自动创建roomid.txt：')
    newsave = open('roomid.txt', 'a')
    newsave.write(roomn)
    newsave.close()


room = live.LiveDanmaku(roomn)  # 直播间

user_id = 3456630  # 默认id值


# 弹幕显示
@room.on('DANMU_MSG')
async def on_danmaku(event):
    global user_id
    user_id = event['data']['info'][2][0]
    # 打印弹幕内容到输出
    print(datetime.datetime.now().strftime('%H:%M:%S'),  # 时间
          ' [弹幕]', event['data']['info'][1],  # 内容
          '\t\t{用户：', event['data']['info'][2][1],  # 用户名
          '，房间：', event['room_display_id'], '}')  # 直播间
    user_id = int(event['data']['info'][2][0])
    try:
        await photo.get_user_face(user_id)
    except:
        pass


# 收到礼物
@room.on('SEND_GIFT')
async def on_gift(event):
    print(datetime.datetime.now().strftime('%H:%M:%S'),
          '【礼物】\t', event['data']['data']['uname'],
          event['data']['data']['action'],
          event['data']['data']['giftName'],
          '\t价值:', event['data']['data']['gold'])
    try:
        await photo.get_user_face(user_id)
    except:
        pass


sync(room.connect())





