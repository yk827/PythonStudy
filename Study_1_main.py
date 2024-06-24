'''我是注释'''
"""我也是注释"""
#我还是注释

str1 = "又来了HELLO World"

print(str1)

age_Wang = 18
print(age_Wang)


breakfast=100
dinner=150
allcash=16000
everyday=allcash/30

print(type(allcash))
print(type(everyday))
print(everyday)
print(round(everyday))
print(type(str1))

print("""
aba
abc
abb
a换行输出
""")

#input只能输入字符串而不能是整形数字
name = input("请输入姓名：")
#birth输入的都是字符串，不是数字
birth = input("出生于何年：")
age_User = 2024 - int(birth)
print("我叫" + name + "出生于" + birth + "，今年" + str(age_User) + "岁。")
#也可以写成下面这样
print(f"{name}你好，你出生于{birth}，今年{age_User}岁")

