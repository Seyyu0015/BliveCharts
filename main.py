import os
import shutil
from bilibili_api import live, sync

import config
import photo
import rank


"""
主方法

"""


# 创建直播间对象
room = live.LiveDanmaku(config.roomid)

# 清空储存用户头像的文件夹以刷新用户头像
shutil.rmtree('./userface')
os.mkdir('./userface')


# 弹幕触发方法
@room.on('DANMU_MSG')
async def on_danmaku(event):
    # 打印弹幕内容到输出
    # print(datetime.datetime.now().strftime('%H:%M:%S'), ' [弹幕]', event['data']['info'][1],
    #       '\t\t{用户：', event['data']['info'][2][1], '，房间：', event['room_display_id'], '}')

    # 获取发送弹幕的用户的信息
    user_id = int(event['data']['info'][2][0])  # 用户id
    user_display_name = event['data']['info'][2][1]  # 用户昵称

    try:
        # 调用增加贡献的方法
        rank.add_user_dict(event['data']['info'][2][1], config.rank_add_by_danmu)
        # 调用爬取头像的方法
        # await photo.get_user_face(user_id, user_display_name)

    except:
        pass


# 礼物触发方法
@room.on('SEND_GIFT')
async def on_gift(event):
    # 打印礼物信息到输出
    # print(datetime.datetime.now().strftime('%H:%M:%S'), '【礼物】\t', event['data']['data']['uname'],
    #       event['data']['data']['action'], event['data']['data']['giftName'], '\t价值:',
    #       event['data']['data']['price'])

    # 根据礼物增加贡献
    try:
        # 修复辣条意外价值为100的问题
        if event['data']['data']['giftName'] == '辣条':
            rank.add_user_dict(event['data']['data']['uname'], 0)
        # 调用增加贡献的方法
        else:
            rank.add_user_dict(event['data']['data']['uname'], event['data']['data']['price'])
        # 调用爬取头像的方法
        # await photo.get_user_face(event['data']['data']['mid'])
    except:
        pass


sync(room.connect())
