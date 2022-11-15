import time
import re
from config import api, token, listen_port, postnamazu_port, config1
from flask import Flask, current_app, redirect, url_for, request
from time import sleep
import json
import config
import requests

# 各个频道
channel_ls = ["/t", "/s", "/p", "/y", "/sh", "/fc", "/b", "/cwl1", "/cwl2", "/cwl3", "/cwl4", "/cwl5"]
channel_name = ["私聊", "说话", "小队", "呼喊", "喊话", "部队", "新人", "跨服贝1", "跨服贝2", "跨服贝3", "跨服贝4",
                "跨服贝5"]

# 实例化app
app = Flask(import_name=__name__)


# 切分频道消息
def message_re(message):
    res = re.search(r'([^@]{1,6})[@\s\S]*:([.。][\s\S]*)', message, re.I)
    return [res.group(1), res.group(2)]


# 请求掷骰结果
def sealdice_api(r, player_name):
    url = api
    body = {"message": r}
    headers = \
        {
            "token": token,
            "Content-Type": "application/json;charset=UTF-8"
        }
    response = requests.post(url, data=json.dumps(body), headers=headers)
    # 返回的不是一个标准的json格式，而类似列表
    dic_res = json.loads("".join(response.text)[:-2][1:])
    time_temp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("[{0}] 海豹返回的掷骰信息: {1}".format(time_temp, dic_res))
    return re.sub(r'<[\s\S]*>', player_name, dic_res["message"], 1)


#
def postnamazu_send(send_m, channel):
    url = "http://127.0.0.1:" + postnamazu_port + "/command"
    # 延后发送1s，不然狒狒会提示“无法在悄悄话、说话、呼喊以及喊话频道连续发言”
    sleep(1)
    if channel == "/t":
        send_mes = "/r" + " " + send_m
    else:
        send_mes = channel + " " + send_m
    requests.post(url, data=send_mes.encode('utf-8'))
    time_temp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("[{0}] 鲶鱼精发送的信息: {1}".format(time_temp, send_m))


# 通过methods设置POST请求
@app.route('/json', methods=["POST"])
def json_request():
    # 接收处理json数据请求
    data = json.loads(request.data)  # 将json字符串转为dict，报这个错误别管了，json效验错误但没什么毛病
    ffmassage = data['ffmassage']
    types = data['types']
    time_temp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("[{0}] 收到来自{1}频道的消息 {2}".format(time_temp, channel_name[channel_ls.index(types)], ffmassage))
    # 切分玩家名和掷骰命令 [玩家名,掷骰命令]
    if ffmassage.find(".") > 0 or ffmassage.find("。") > 0:
        ls_receive = message_re(ffmassage)
        dice_result = sealdice_api(ls_receive[1], ls_receive[0])
        postnamazu_send(dice_result, types)
    return "ffmassage = %s types = %s" % (ffmassage, types)


if __name__ == '__main__':
    print('''  ______ ________   _________      __   _______ _____  _____   _____     _____ _____ _____ ______ 
 |  ____|  ____\ \ / /_   _\ \    / /  |__   __|  __ \|  __ \ / ____|   |  __ \_   _/ ____|  ____|
 | |__  | |__   \ V /  | |  \ \  / /      | |  | |__) | |__) | |  __    | |  | || || |    | |__   
 |  __| |  __|   > <   | |   \ \/ /       | |  |  _  /|  ___/| | |_ |   | |  | || || |    |  __|  
 | |    | |     / . \ _| |_   \  /        | |  | | \ \| |    | |__| |   | |__| || || |____| |____ 
 |_|    |_|    /_/ \_\_____|   \/         |_|  |_|  \_\_|     \_____|   |_____/_____\_____|______|
                                                                            by 华采衣兮若英 @萌芽池   
                                                                                                  
                                 本程序主页与教程可见 https://github.com/kagangtuya-star/FFxivTrpgDice
                                 ''')
    print("读取配置信息如下：")
    print(config1)
    app.run(port=17777)
