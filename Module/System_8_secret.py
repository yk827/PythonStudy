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
