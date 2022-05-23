from bs4 import BeautifulSoup

"""更新显示页面。

改变“display_html.html”的图片地址和文本内容
"""


def display_change(num: int, img_src: str, con: int):
    """将第num个图片替换为 img_src；将第num个文字替换为Con。

    :param num: 排名
    :param img_src: 图片本地地址
    :param con: 贡献值
    :return:
    """
    with open("display_html.html", "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

        # 修改图片
        img = soup.find('img', id='img' + str(num))
        img['src'] = 'userface/' + img_src

        # 修改文字
        text = soup.find('div', id='text' + str(num))
        text.string = str(con)

        # 防止页面出现乱码
        meta = soup.find('meta')
        meta['charset'] = 'gb18030'

    # 写入文件
    with open("display_html.html", "w") as fh:
        fh.write(soup.prettify())


def reset():
    """清空显示页面.

    :return:
    """
    # 从预设空页面获取信息
    with open("display_html_null.html", "r") as f_null:
        contents_null = f_null.read()
        soup_null = BeautifulSoup(contents_null, 'lxml')
        # 防止页面出现乱码
        meta_null = soup_null.find('meta')
        meta_null['charset'] = 'gb18030'

    # 写入文件
    with open("display_html.html", "w") as fh:
        fh.write(soup_null.prettify())
