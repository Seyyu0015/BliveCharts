# 哔哩哔哩直播图表
## 简介
这是一款在OBS内使用的直播插件，目前包含以下功能  
* 观众互动排行  
* 弹幕高频字分析
## 观众互动排行
### 简介
连接到Bilibili直播间后，对直播间观众的互动行为进行量化统计并排名，之后以《我的世界》风格展示给观众。  
### 使用效果展示  
下方的“物品栏”中会显示贡献值前9的观众的头像和贡献值  
![使用效果图](https://user-images.githubusercontent.com/103107612/169229142-e69fda12-539b-42a4-9fc0-c818ea056d6a.png)  
视频展示:[《Minecraft》风格的“直播贡献榜”使用效果展示](https://www.bilibili.com/video/BV1jr4y1t71Q/)
### 如何使用
1. 在“config.py”文件中配置直播间ID  
2. 打开“style.css”文件，复制全部内容  
3. 打开OBS 添加“浏览器源” 勾选本地文件并选择“display_html.html”文件   
    - 宽度： 740  
    - 高度： 97  
    - 自定义css：粘贴（第2步中复制的内容）  
4. 点击“确定”插件就会出现在舞台内  
5. 运行“main.py”  
### 配置文件
项目根目录中的“config.py”文件 (变量名 = 默认值 # 描述)
* roomid = 8763308  # 直播间id，程序会连接到该直播间.(默认值=8763308)
* rank_add_by_danmu = 1  # 每发送一个弹幕所增加的贡献值.(默认值=1)
* free_gift = 1  # 免费礼物增加的贡献值.(默认值=1)
* price = 100  # 礼物价值和增加贡献的比值.(默认值=100)
* number = 9  # 排行榜显示个数.(默认值=9)



## 弹幕高频字分析
### 简介
自动保存直播中的弹幕信息，统计每个汉字的出现频率，渲染为柱状图并保存  
* danmusave/txt 保存弹幕文本的文件夹  
* danmusave/png 保存柱状图的文件夹
### 使用效果展示
2022年5月13日的弹幕频率图  
![弹幕频率图](https://user-images.githubusercontent.com/103107612/169229650-0c69052f-e3e6-430b-b12e-c15329780c04.png)  

### 如何使用
1. 修改项目根目录中的“config.py”文件  
+ 使以下两项均为True (变量名 = 默认值 # 描述)  
  - save_danmu = True # 是否保存弹幕(默认值=True)
  - danmu_bar = True # 是否分析弹幕(默认值=True)
+ 使“roomid”为想要连接的直播间
   - roomid = 8763308  # 直播间id，程序会连接到该直播间。
2. 运行“main.py”
3. 生成的文本存档和柱状图会保存在相应目录内
### 其他  
* 可能因为爬取头像过于频繁导致暂时无法获取头像，数小时后恢复  

