"""
主方法

"""
import datetime
import os
import shutil
from bilibili_api import live, sync
import photo
import rank

try:
    roomid = open('roomid.txt', 'r')
    roomn = int(roomid.read())
    roomid.close()
except:
    print('未从roomid.txt中获取信息')
    roomn = input('输入房间号来自动创建roomid.txt：')
    newsave = open('roomid.txt', 'a')
    newsave.write(roomn)
    newsave.close()
room = live.LiveDanmaku(roomn)

"""
+user_id：默认的用户id。
+rank_add_by_danmu：每发送一个弹幕所增加的贡献值。
"""
user_id = 3456630
rank_add_by_danmu = 1

# 清空文件夹以刷新用户头像
shutil.rmtree('./userface')
os.mkdir('./userface')


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
        rank.add_user_dict(user_id, rank_add_by_danmu)
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
          '\t价值:', event['data']['data']['price'])
    print(event)
    try:
        if event['data']['data']['giftName'] == '辣条':
            rank.add_user_dict(user_id, 0)
        else:
            rank.add_user_dict(user_id, event['data']['data']['price'])
        await photo.get_user_face(user_id)
    except:
        pass


sync(room.connect())
