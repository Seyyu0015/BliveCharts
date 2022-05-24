import re

import matplotlib.pyplot as plt
from pylab import mpl

"""绘图脚本。

绘制弹幕频率柱状图
"""

global FILE_TIME


def read_file(danmu_time):
    """统计以danmu_time开头的弹幕存档文件.

    :param danmu_time: 日期
    :return: 单字频率排名
    """
    global FILE_TIME
    FILE_TIME = danmu_time

    with open('danmusave/txt/' + FILE_TIME + 'danmu.txt', 'r') as f:
        # 空字典用来存储文本中的单字
        word = {}

        # 清除符号
        for word_str in f.readlines():
            word_str = re.sub('[^\u4e00-\u9fa5]+', '', word_str)

            # 统计字数
            for i in word_str:
                if i in word:
                    word[i] += 1
                else:
                    word[i] = 1

        # 排名字数
        rank_list = sorted(word.items(), key=lambda x: x[1], reverse=True)
        return rank_list


def show_rank(rank_list):
    """根据read_file读取的信息绘制柱状图.

    :param rank_list: 单字频率排名
    :return:
    """
    # 设置显示中文字体
    mpl.rcParams["font.sans-serif"] = ["SimHei"]

    # 准备数据
    x_bar_text = []
    y_bar_num = []

    # 显示的个数
    show_num = 5
    for i in rank_list:
        x_bar_text.append(i[0])
        y_bar_num.append(i[1])
        show_num -= 1
        if show_num == 0:
            break

    # 绘制柱状图
    plt.bar(x_bar_text, y_bar_num)
    plt.ylabel('出现次数')
    title = '弹幕单字频率   ' + FILE_TIME
    plt.title(title)
    plt.savefig('danmusave/png/' + FILE_TIME + 'danmu.png')
    plt.show()


def rank(danmu_time):
    show_rank(read_file(danmu_time))
