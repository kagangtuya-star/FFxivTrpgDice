# main.py
import json


def read_config():
    """"读取配置"""
    with open("config.json") as json_file:
        config = json.load(json_file)
    return config


# def update_config(config):
#     """"更新配置"""
#     with open("config.json", 'w') as json_file:
#         json.dump(config, json_file, indent=4)
#     return None

api = ''
token = ''
listen_port = ''
postnamazu_port = ''
config1 = read_config()
globals().update(config1)  # 转化为全局变量
api = api + "/sd-api/dice/exec"
