import config
import display

"""排名处理。

用于保存和计算用户排名
"""

user_dict = {}  # 初始化数组


def add_user_dict(name, number):
    """为用户增加积分的方法

    :param name: 用户的昵称
    :param number: 增加的贡献值
    :return:
    """

    # 免费礼物价值
    if number == 0:
        number = config.free_gift

    if name in user_dict:
        user_dict[name] += number
    else:
        user_dict[name] = number

    # 打印排名
    print('\n\n\n\n[Rank][add_user_dict]用户', name, '，贡献值增加：', number)
    show_user_rank(sort_dict(user_dict))


def sort_dict(d):
    """排序存储用户贡献的字典为列表。

    :param d: 储存用户贡献的字典
    :return: 排名列表
    """

    rank_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return rank_list


def show_user_rank(ls):
    """打印排名信息。

    :param ls: 打印的列表
    :return:
    """
    print('============贡献榜============')
    print('%-4s%-7s%-10s' % ('│排名', '│贡献', '│用户'))
    i = 1
    for item in ls:
        if i <= config.number:
            text1 = '│' + str(i)
            text2 = '│' + str(item[1])
            text3 = '│' + str(item[0])
            print('%-5s%-8s%-10s' % (text1, text2, text3))
            display.display_change(i, str(item[0]) + '.png', int(item[1]))
            i += 1
        else:
            print('│......')
            if config.number != 0:
                break
    print('—————————————————————————————')
