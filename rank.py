"""
排名控制

+freegift： 免费礼物增加的贡献值,0为不增加。
"""
freegift = 1

user_dict = {}  # 初始化数组


# 增加排行字典 为 mid的用户增加 number积分
def add_user_dict(mid: int, number: int):
    # 免费礼物价值
    if number == 0:
        number = freegift

    if mid in user_dict:
        user_dict[mid] += number
    else:
        user_dict[mid] = number
    # 打印排名
    show_user_rank(sort_dict(user_dict), 8)


# 对字典d进行排序 返回列表
def sort_dict(d):
    rank_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return rank_list


# print排名信息 列表名ls 显示个数number（前number个）
def show_user_rank(ls, number):
    print('============贡献榜============')
    i = 1
    for item in ls:
        if i <= number:
            text1 = '│第' + str(i) + '名:' + str(item[0])
            text2 = '│贡献:' + str(item[1])
            print('%-20s%-10s' % (text1, text2))
            i += 1
        else:
            break
    print('-----------------------------')
