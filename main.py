import time

from bilibili_api import live, sync, user

import photo
import rank
import config
import display
import danmu_bar

"""主方法。

连接直播间并调用其他模块
"""

# 初始化
room = live.LiveDanmaku(config.roomid)  # 创建直播间
time = time.strftime("%Y-%m-%d_", time.localtime())  # 获取当前时间
display.reset()  # 重置页面


@room.on('DANMU_MSG')
async def on_danmaku(event):
    """检测到弹幕时触发的方法。

    :param event: 弹幕对象
    :return:
    """
    # 根据弹幕获得信息
    user_id = int(event['data']['info'][2][0])
    user_name = event['data']['info'][2][1]
    danmu_text = event['data']['info'][1]

    # 分析弹幕
    if config.save_danmu:
        with open('danmusave/txt/' + time + 'danmu' + '.txt', "a") as f:
            f.write(danmu_text)
        if config.danmu_bar:
            danmu_bar.rank(time)

    # 爬取头像并增加贡献
    # noinspection PyBroadException
    try:
        await photo.face_download_by_danmu(user.User(user_id))
        rank.add_user_dict(user_name, config.rank_add_by_danmu)
    except:
        pass


@room.on('SEND_GIFT')
async def on_gift(event):
    """检测到礼物时触发的方法。

    :param event: 礼物对象
    :return:
    """
    # 根据礼物获得信息
    user_name = event['data']['data']['uname']  # 用户昵称
    user_face = event['data']['data']['face']  # 用户头像网络地址
    gift_name = event['data']['data']['giftName']  # 礼物名称
    gift_price = event['data']['data']['price']  # 礼物价值
    gift_num = event['data']['data']['num']  # 礼物数量
    total_price = gift_price * gift_num / config.price  # 总计贡献值

    # 调用爬取头像的方法
    await photo.face_download_by_gift(user_name, user_face)

    # 调用增加贡献的方法
    # noinspection PyBroadException
    try:
        if gift_name == '辣条' or gift_name == '小心心':
            rank.add_user_dict(user_name, config.free_gift * gift_num)
        else:
            rank.add_user_dict(user_name, total_price)
    except:
        pass


sync(room.connect())
