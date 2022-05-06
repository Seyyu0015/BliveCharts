from pyecharts import *
from pyecharts.charts import Bar

if __name__ == '__main__':

    bar = Bar("成绩柱形图", "副标题")
    # 用于添加图表的数据和设置各种配置项
    # is_more_utils=True可以按右边的下载按钮将图片下载到本地

    bar.add("成绩表", ["语文", "数学", "英语", "物理", "化学", "生物"], [88, 90, 92, 87, 83, 81], is_more_utils=True)
    bar.show_config()  # 打印输出图表的所有配置项
    bar.render('E:\\pye\\bar.html')  # 在指定目录下生成一个 bar.html 的文件
