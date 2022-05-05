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
    show_user_rank(sort_dict(user_dict))


# 对字典d进行排序 返回列表
def sort_dict(d):
    rank_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return rank_list


# print排名信息 列表名ls 显示个数number（前number个）
def show_user_rank(ls):
    print('============贡献榜============')
    print('%-4s%-7s%-10s' % ('│排名', '│贡献', '│用户'))
    i = 1
    v = 1
    for item in ls:
        if i <= config.number or config.number == 0:
            text1 = '│' + str(v)
            text2 = '│' + str(item[1])
            text3 = '│' + str(item[0])
            print('%-5s%-8s%-10s' % (text1, text2, text3))
            v += 1
            if config.number != 0:
                i += 1
        elif i == config.number+1:
            print('......')
            break
    print('-----------------------------')
