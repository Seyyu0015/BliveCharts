import urllib

from bilibili_api import user, sync

"""提供获取用户信息的方法"""

'''
创建用户对象后再调用保存头像的方法
user = user.User(84125742)
'''


# 保存用户的头像
async def get_user_face(user):
    urlStr = sync(user.get_user_info())['face']
    mid = str(sync(user.get_user_info())['mid'])
    urllib.request.urlretrieve(urlStr, filename='./userface/' + mid + '.png')
