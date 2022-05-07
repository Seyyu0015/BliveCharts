#!/usr/bin/python3
from bs4 import BeautifulSoup


# 刷新显示页面的方法 将第num个图片替换为 img_src；将第num个文字替换为Con
def display_change(num: int, img_src: str, con: int):
    with open("display_html.html", "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

        img = soup.find('img', id='img' + str(num))
        img['src'] = 'userface/' + img_src

        text = soup.find('td', id='text' + str(num))
        text.string = str(con)

        meta = soup.find('meta')
        meta['charset'] = 'gb18030'

    with open("display_html.html", "w") as fh:
        fh.write(soup.prettify())


if __name__ == '__main__':
    display_change(1, '冰糖糯米.png', 2)
