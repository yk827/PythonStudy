#字典的key-value对可以是任意的对象，而不仅仅是字符串。
#key可以是数字、元组、列表等任意不可变对象，而value可以是任意对象。两者具有一一对应的映射关系
#字典的key-value对可以动态添加、删除、修改。

#字典的key是唯一的，不能重复。如果试图将一个已经存在的key赋值给字典，则会覆盖原来的value。


#创建字典
my_dict = {
    'apple': 10,
    'banana': 20,
    'orange': 30
    }

#访问字典元素
print(my_dict['apple'])  #输出10

#修改字典元素
my_dict['apple'] = 15
print(my_dict['apple'])  #输出15


#添加字典元素
my_dict['grape'] = 40
print(my_dict)  #输出{'apple': 15, 'banana': 20, 'orange': 30, 'grape': 40}


#删除字典元素
del my_dict['banana']
print(my_dict)  #输出{'apple': 15, 'orange': 30, 'grape': 40}

#判断字典是否为空
if my_dict:
    print("字典不为空")
else:
    print("字典为空")


#字典的key-value对可以是任意的对象，而不仅仅是字符串。
my_dict['color'] = ["红色", "黄色", "绿色"]
print(my_dict)  #输出{'apple': 15, 'orange': 30, 'grape': 40, '荔枝': ['红色', '黄色', '绿色']}
print(my_dict['color'][1])  #输出'黄色'

my_dict['color'][0] = "蓝色"
print(my_dict)  #输出{'apple': 15, 'orange': 30, 'grape': 40, '荔枝': ['蓝色', '黄色', '绿色']}

my_dict['color'].append("紫色")
print(my_dict)  #输出{'apple': 15, 'orange': 30, 'grape': 40, '荔枝': ['蓝色', '黄色', '绿色', '紫色']}

my_dict['color'].remove("黄色")
print(my_dict)  #输出{'apple': 15, 'orange': 30, 'grape': 40, '荔枝': ['蓝色', '绿色', '紫色']}

my_dict['color'] = "红色"
print(my_dict)  #输出{'apple': 15, 'orange': 30, 'grape': 40, 'color': '红色'}

my_dict['color'] = ["红色", "黄色", "绿色"]
print(my_dict)  #输出{'apple': 15, 'orange': 30, 'grape': 40, 'color': ['红色', '黄色', '绿色']}

#循环输出字典的key-value对
for key, value in my_dict.items():
    print(f"水果：{key}，数量： {value}")

for items in my_dict.items():
    print(items)

#删除葡萄
my_dict.pop('grape')
print(my_dict)  #输出{'apple': 15, 'orange': 30, 'color': ['红色', '黄色', '绿色']}
#默认删除最后一个
my_dict.popitem()
print(my_dict)  #输出{'apple': 15, 'orange': 30}
#删除所有元素
my_dict.clear()
print(my_dict)  #输出{}

