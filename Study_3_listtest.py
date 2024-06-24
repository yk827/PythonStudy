#列表的定义需要用方括号  []
student = ["赵","钱","孙","李"]

print(student[1])
print(student[-1])
print(type(student[1]))

print(len(student))

#1:3的时候不读取最后一个，相当于3是开区间
print(student[1:3])
print(student[1:])
print(student[:3])

#字串转为队列
poem = "沉舟侧畔千帆过"
print(len(poem))
data = "2024.6.14"
print(data.split("."))

#队列转为字符串
str1 = "14,6,2024"
print(",".join(str1))
str2 = ["14","6","2024"]
print("/".join(str2))



#修改列表内容
student[1] = "7"
print(student)

#锁定列表，将方括号[]改为圆括号()变为tuple元组
student2 = ("周","吴","郑","王")
#student2[3] = "喵"
print(student2)

#新增列表
student.append("周")
print(student)
student.extend(["冯", "陈"])
print(student)

#删除
student.remove("7")
print(student)

student.pop(3)
print(student)

#判断是否存在列表中
Xing1 = input("你要删：")
if Xing1 in student:
    student.remove(Xing1)
    print(student)
else:
    print("这人不在这")



Xing2 = input("你要加")
if Xing2 not in student:
    student.append(Xing2)
    print(student)
    print(student.index(Xing2) + 1)
else:
    print(student.index(Xing2))


