import datetime

import config

"""
排名控制

"""

user_dict = {}  # 初始化数组


# 增加排行字典 为 mname的用户增加 number积分
def add_user_dict(mname, number: int):
    # 免费礼物价值
    if number == 0:
        number = config.freegift

    if mname in user_dict:
        user_dict[mname] += number
    else:
        user_dict[mname] = number
    # 打印排名
    print('\n\n\n\n[Rank][add_user_dict]用户', mname, '，贡献值增加：', number)
    show_user_rank(sort_dict(user_dict))


# 对字典d进行排序 返回rank_list列表
def sort_dict(d):
    rank_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return rank_list


# print排名信息 列表名ls 显示个数number（前number个）
def show_user_rank(ls):
    print('============贡献榜============')
    print('%-4s%-7s%-10s' % ('│排名', '│贡献', '│用户'))
    i = 1
    for item in ls:
        if i <= config.number:
            text1 = '│' + str(i)
            text2 = '│' + str(item[1])
            text3 = '│' + str(item[0])
            print('%-5s%-8s%-10s' % (text1, text2, text3))
            i += 1
        else:
            print('│...')
            if config.number != 0:
                break
    print('—————————————————————————————')
