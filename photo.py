import urllib

"""用户头像模块。

用于下载并保存用户的头像。
"""


async def face_download_by_danmu(user_obj):
    """通过检测弹幕获取用户头像。

    :param user_obj: 用户对象
    :return:
    """
    user_info = await user_obj.get_user_info()
    user_name = user_info['name']
    user_face = user_info['face']
    await face_download_by_gift(user_name, user_face)


async def face_download_by_gift(user_name, user_face):
    """通过检测礼物获取用户头像。

    :param user_name: 用户的昵称
    :param user_face: 用户头像的网络地址
    :return:
    """
    path = './userface/'

    # noinspection PyBroadException
    try:
        urllib.request.urlretrieve(user_face, filename=path + user_name + '.png')
    except:
        pass
