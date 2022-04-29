"""按观众的贡献进行排名和记录"""
user_dict = {}
freegift = 1  # 免费礼物增加的贡献值,0为不增加


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


# 用于测试的方法
if __name__ == '__main__':
    e = {'room_display_id': 21925332, 'room_real_id': 21925332, 'type': 'SEND_GIFT', 'data': {'cmd': 'SEND_GIFT', 'data': {'action': '投喂', 'batch_combo_id': 'batch:gift:combo_id:24358957:17661166:30606:1651203669.3940', 'batch_combo_send': {'action': '投喂', 'batch_combo_id': 'batch:gift:combo_id:24358957:17661166:30606:1651203669.3940', 'batch_combo_num': 1, 'blind_gift': None, 'gift_id': 30606, 'gift_name': '泡泡机', 'gift_num': 1, 'send_master': None, 'uid': 24358957, 'uname': '橘色狸花猫2333'}, 'beatId': '', 'biz_source': 'Live', 'blind_gift': None, 'broadcast_id': 0, 'coin_type': 'gold', 'combo_resources_id': 1, 'combo_send': {'action': '投喂', 'combo_id': 'gift:combo_id:24358957:17661166:30606:1651203669.3909', 'combo_num': 1, 'gift_id': 30606, 'gift_name': '泡泡机', 'gift_num': 1, 'send_master': None, 'uid': 24358957, 'uname': '橘色狸花猫2333'}, 'combo_stay_time': 3, 'combo_total_coin': 5000, 'crit_prob': 0, 'demarcation': 2, 'discount_price': 5000, 'dmscore': 120, 'draw': 0, 'effect': 0, 'effect_block': 0, 'face': 'http://i1.hdslb.com/bfs/face/7b09b025531925baccb6769d86318aa65dcf966a.jpg', 'float_sc_resource_id': 0, 'giftId': 30606, 'giftName': '泡泡机', 'giftType': 0, 'gold': 0, 'guard_level': 3, 'is_first': True, 'is_special_batch': 0, 'magnification': 1, 'medal_info': {'anchor_roomid': 0, 'anchor_uname': '', 'guard_level': 3, 'icon_id': 0, 'is_lighted': 1, 'medal_color': 1725515, 'medal_color_border': 6809855, 'medal_color_end': 5414290, 'medal_color_start': 1725515, 'medal_level': 22, 'medal_name': '克苏玲', 'special': '', 'target_id': 17661166}, 'name_color': '#00D1F1', 'num': 1, 'original_gift_name': '', 'price': 5000, 'rcost': 20791724, 'remain': 0, 'rnd': '1651203669121700001', 'send_master': None, 'silver': 0, 'super': 0, 'super_batch_gift_num': 1, 'super_gift_num': 1, 'svga_block': 0, 'tag_image': '', 'tid': '1651203669121700001', 'timestamp': 1651203669, 'top_list': None, 'total_coin': 5000, 'uid': 24358957, 'uname': '橘色狸花猫2333'}}}

    print(e['data']['data']['giftName'])
