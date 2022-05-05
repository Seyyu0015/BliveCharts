import os
import urllib
from bilibili_api import user


"""
用户信息

"""


# 保存用户的头像
async def face_download(usera):
    user_info = await usera.get_user_info()
    urlstr = user_info['face']
    mid = user_info['name']
    path = './userface/'
    try:
        urllib.request.urlretrieve(urlstr, filename=path + mid + '.png')
        print('[Photo][下载成功]', str(user_info['mid']))
    except:
        print('[Photo][下载失败]', str(user_info['mid']))


# 防止重复下载
async def get_user_face(user_id_getface, user_display_name):
    path = './userface/'
    file_name_list = os.listdir(path)
    # 如果没有任何头像已保存，跳过检测
    if not file_name_list:
        await face_download(user.User(user_id_getface))

    else:
        exphoto = False
        for filename in file_name_list:
            if filename == user_display_name + '.png':
                exphoto = True
                break
        # 下载头像
        if not exphoto:
            print('[Photo][尝试下载]', str(user_id_getface))
            await face_download(user.User(user_id_getface))
