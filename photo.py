import os
import urllib

from bilibili_api import user, sync

"""提供获取用户信息"""

'''
创建用户对象后再调用保存头像的方法
get_user_face(user.User(84125742))
'''

user_id = 84125742


# 保存用户的头像
def face_download(usera):
    urlstr = sync(usera.get_user_info())['face']
    mid = str(sync(usera.get_user_info())['mid'])
    path = './userface/'
    urllib.request.urlretrieve(urlstr, filename=path + mid + '.png')


# 防止重复下载
def get_user_face(user_id_getface):
    path = './userface/'
    file_name_list = os.listdir(path)
    # 如果没有任何头像已保存，跳过检测
    if not file_name_list:
        face_download(user.User(user_id_getface))
        print('null')

    else:
        for filename in file_name_list:
            if filename == str(user_id_getface) + '.png':
                break
            # 下载头像
            print('下载')
            face_download(user.User(user_id_getface))


# 测试下载的方法
if __name__ == "__main__":
    get_user_face(84125742)
