from bilibili_api import live, sync, user
import config
import display
import photo
import rank

"""
主方法

"""

# 创建直播间对象
room = live.LiveDanmaku(config.roomid)

# 重置html文件
display.reset()


# 弹幕触发方法
@room.on('DANMU_MSG')
async def on_danmaku(event):
    # 根据弹幕获得信息
    user_id = int(event['data']['info'][2][0])
    user_name = event['data']['info'][2][1]

    print(user_id, user_name)
    try:
        # 调用爬取头像的方法
        await photo.face_download_by_danmu(user.User(user_id))
        # 调用增加贡献的方法
        rank.add_user_dict(user_name, config.rank_add_by_danmu)

    except:
        pass


# 礼物触发方法
@room.on('SEND_GIFT')
async def on_gift(event):
    # 根据礼物获得信息
    user_name = event['data']['data']['uname']
    user_face = event['data']['data']['face']
    gift_name = event['data']['data']['giftName']
    gift_price = event['data']['data']['price']
    gift_num = event['data']['data']['num']

    # 调用爬取头像的方法
    await photo.face_download_by_gift(user_name, user_face)

    # 根据礼物数量和价值计算总贡献
    total_price = gift_price * gift_num / config.price

    # 调用增加贡献的方法
    try:
        if gift_name == '辣条':
            rank.add_user_dict(user_name, config.free_gift * gift_num)
        else:
            rank.add_user_dict(user_name, total_price)

    except:
        pass


sync(room.connect())
