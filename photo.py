import os
import urllib

from bilibili_api import user, sync

"""提供获取用户信息"""


# 保存用户的头像
async def face_download(usera):
    user_info = await usera.get_user_info()
    urlstr = user_info['face']
    mid = str(user_info['mid'])
    path = './userface/'
    try:
        urllib.request.urlretrieve(urlstr, filename=path + mid + '.png')
        print('下载成功')
    except:
        print('下载失败')


# 防止重复下载
async def get_user_face(user_id_getface):
    path = './userface/'
    file_name_list = os.listdir(path)
    # 如果没有任何头像已保存，跳过检测
    if not file_name_list:
        await face_download(user.User(user_id_getface))

    else:
        for filename in file_name_list:
            if filename == str(user_id_getface) + '.png':
                break
            # 下载头像
            print('Photo：尝试下载' + str(user_id_getface))
            await face_download(user.User(user_id_getface))


# 测试下载的方法
# if __name__ == "__main__":
#     get_user_face(84125742)
