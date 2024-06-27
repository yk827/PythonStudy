wang={
    'name':'wang',
    'age':25,
    'gender':'male',
    'hobby':'reading'
}

li={
    'name':'li',
    'age':23,
    'gender':'female',
    'hobby':'swimming'
}

zhang={
    'name':'zhang',
    'age':22,
    'gender':'male',
    'hobby':'running'
}

zhao={
    'name':'zhao',
    'age':24,
    'gender':'male',
    'hobby':'swimming'
}

students=[wang,li,zhang,zhao]

stu = input("请输入学生姓名：")

#str(students)将列表转化为字符串，再用in判断是否包含该学生，但是方法不太好，因为列表中可能有字典，字典中可能有列表，所以不能直接用in判断
'''if stu in str(students):
    for i in students:

        print(i)#i是字典,打印字典中所有学生信息
        if i['name'] == stu:
            print("姓名：",i['name'])
            print("年龄：",i['age'])
            print("性别：",i['gender'])
            print("爱好：",i['hobby'])

else:
    print("没有该学生信息！")'''


# 改进方法：用for循环遍历列表，用if判断字典中的name是否等于输入的学生姓名，如果等于，则打印该学生信息并退出循环，否则继续循环
found = False
for i in students:
    if i['name'] == stu:
        found = True
        print("姓名：", i['name'])
        print("年龄：", i['age'])
        print("性别：", i['gender'])
        print("爱好：", i['hobby'])
        break  # 找到学生后立即退出循环
else:
    print("没有该学生信息！")