# BililiveContributionRank
连接Bilibili直播间，对用户互动行为量化统计并排行，并以《我的世界》风格在OBS内作为插件展示给观众。
![OBS内效果](https://user-images.githubusercontent.com/103107612/167257703-1c2f0aa7-ef76-4675-ad16-22aa8343eacb.png)

# 视频展示
 哔哩哔哩：https://www.bilibili.com/video/BV1jr4y1t71Q/

# 使用插件
![输入id](https://user-images.githubusercontent.com/103107612/167257797-88d416ea-b11e-4040-8a75-d351af61d289.png)

1.在“config.py”文件中配置直播间ID

2.打开“style.css”文件，复制全部内容

3.打开OBS 添加“浏览器源” 勾选本地文件并选择“display_html.html”文件

宽度： 740
高度： 97
  
在“自定义css”中粘贴第2部中复制的内容
点击“确定”插件就会出现在舞台内

4.运行“main.py”

# 其他
1.如果直播间太火可能因为爬取头像过于频繁导致暂时封禁

2.“运行”中会输出更详细的排名信息

3.可以从“config.py”中分别配置每条弹幕和免费礼物增加的贡献值

![控制台输出更详细](https://user-images.githubusercontent.com/103107612/167257982-18849e35-c38d-4e50-acd2-0bac44809ef6.png)
