import random
import string
num = string.digits#产生数字
alp = string.ascii_lowercase#小写字母
alp_u = string.ascii_uppercase#大写字母
chac = string.ascii_letters#产生英文字母

Secret1 =list(num+chac)
random.shuffle(Secret1)
print(Secret1)


Secret2 =num+chac
random.shuffle(list(Secret2))
print(Secret2)

length = input("请输入密码长度：")
Secret3 = "".join(Secret1[:int(length)])
print(f"随机密码：{Secret3}")


import requests
import json
city = input("请输入城市名称：")
api = "27fddef8fc277d3ae2237e5f36ff347b"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
'''wheather_data = requests.get(url)
print(wheather_data.json()["main"]["temp"]) '''
response = requests.get(url)

if response.status_code == 200:
    wheather_data = response.json()
    try:
        temperature = wheather_data["main"]["temp"] - 273.15
        print(f"当前温度是：{temperature:.2f}°C")
    except KeyError:
        print("无法获取温度数据")
else:
    print(f"请求失败，状态码：{response.status_code}")