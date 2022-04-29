"""按观众的贡献进行排名和记录"""
user_dict = {}


# 增加排行字典 为 mid的用户增加 number积分
def add_user_dict(mid, number):
    if mid in user_dict:
        user_dict[mid] += number
    else:
        user_dict[mid] = number


# 对字典d进行排序 返回列表
def sort_dict(d):
    rank_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return rank_list


# print排名信息 列表名ls 显示个数number（前number个）
def show_user_rank(ls, number):
    print('===========贡献榜===========')
    i = 1
    for item in ls:
        if i <= number:
            print('│第' + str(i) + '名', str(item[0]) + '   │贡献', item[1], sep=':')
            i += 1
        else:
            break
    print('---------------------------')


# 用于测试的方法
if __name__ == '__main__':
    add_user_dict(1111111, 1)
    add_user_dict(2222222, 6)
    add_user_dict(1111111, 2)
    show_user_rank(sort_dict(user_dict), 1)
