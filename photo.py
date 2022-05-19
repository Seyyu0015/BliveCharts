import urllib

"""
用于下载用户头像的脚本

"""


# 通过弹幕 保存用户的头像
async def face_download_by_danmu(user_obj):
    user_info = await user_obj.get_user_info()
    user_name = user_info['name']
    user_face = user_info['face']
    await face_download_by_gift(user_name, user_face)


# 通过礼物 保存用户的头像
async def face_download_by_gift(user_name, user_face):
    path = './userface/'
    # noinspection PyBroadException
    try:
        urllib.request.urlretrieve(user_face, filename=path + user_name + '.png')
    except:
        pass
