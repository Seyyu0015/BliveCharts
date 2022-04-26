import os
import urllib

from bilibili_api import user, sync

"""提供获取用户信息的方法"""

'''
创建用户对象后再调用保存头像的方法
user = user.User(84125742)
'''


# 保存用户的头像
def get_user_face(user):
    urlstr = sync(user.get_user_info())['face']
    mid = str(sync(user.get_user_info())['mid'])
    path = './userface/'
    file_name_list = os.listdir(path)
    # 查找是否已下载头像
    # TODO:文件夹为空时无法正常运行
    for filename in file_name_list:
        if filename == mid + '.png':
            break
        # 下载头像
        print('下载')
        urllib.request.urlretrieve(urlstr, filename=path + mid + '.png')


# 测试下载的方法
if __name__ == "__main__":
    get_user_face(user.User(5294454))
