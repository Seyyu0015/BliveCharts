import datetime
import photo
from bilibili_api import user, live, sync

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

room = live.LiveDanmaku(roomn)
data = 'danmusave\danmusave' + datetime.datetime.now().strftime('%y%m%d%H%M%S') + '.txt'


# 弹幕显示
@room.on('DANMU_MSG')
async def on_danmaku(event):
    danmusave = open(data, 'a')
    danmusave.write(datetime.datetime.now().strftime('%H:%M:%S'))
    danmusave.write('\t')
    danmusave.write(event['data']['info'][1])
    danmusave.write('\t')
    danmusave.write(event['data']['info'][2][1])
    danmusave.write('\t')
    danmusave.write(event['room_display_id'])
    danmusave.write('\n')

    danmusave.close()

    print(datetime.datetime.now().strftime('%H:%M:%S'),  # 时间
          ' [弹幕]', event['data']['info'][1],  # 内容
          '\t\t{用户：', event['data']['info'][2][1],  # 用户名
          '，房间：', event['room_display_id'], '}')  # 直播间


# 收到礼物
@room.on('SEND_GIFT')
async def on_gift(event):
    print(datetime.datetime.now().strftime('%H:%M:%S'),
          '【礼物】\t', event['data']['data']['uname'],
          event['data']['data']['action'],
          event['data']['data']['giftName'],
          '\t价值:', event['data']['data']['gold'])


sync(room.connect())
