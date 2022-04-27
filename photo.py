import os
import urllib

from bilibili_api import user, sync

"""提供获取用户信息"""

'''
创建用户对象后再调用保存头像的方法
get_user_face(user.User(84125742))
'''

doget = 0
user_id = 84125742


# 保存用户的头像
def face_download(urlstr, mid):
    path = './userface/'
    urllib.request.urlretrieve(urlstr, filename=path + mid + '.png')


# 防止重复下载
def get_user_face(user):
    urlstr = sync(user.get_user_info())['face']
    mid = str(sync(user.get_user_info())['mid'])
    path = './userface/'
    file_name_list = os.listdir(path)
    if not file_name_list:
        face_download(urlstr, mid)
        print('null')

    else:
        for filename in file_name_list:
            if filename == mid + '.png':
                break
            # 下载头像
            print('下载')
            face_download(urlstr, mid)


# 测试下载的方法
if __name__ == "__main__":
    get_user_face(user.User(user_id))
