def Hello(name, age):
    print("Hello, 我叫", name, "，我今年", age, "岁了！")

Hello("John", 25)
Hello(age=30, name="Mary")
#函数测试


count = 0.9
def total(price, transaction=25):
    i = 0.5
    return price * count + transaction
#return 放在函数的最后，用于终止函数，下面的print语句不会被执行。
    print("这件衣服的总金额是", total(100, 50), "元。")
print(f"这件衣服的总金额是{total(100, 50)}元。")


#全局变量和局部变量
#全局变量：在函数内部定义的变量，不管函数是否调用，都可以访问到。
#局部变量：在函数内部定义的变量，只在函数内部有效，函数调用后，变量将被销毁。
print(f"全局变量count的值是{count}。")
#print(f"局部变量i的值是{i}。") #此处会报错，因为i是局部变量，函数调用后，变量将被销毁。
#在i 前加入global 关键字，可以访问全局变量，就能访问了，但不建议这么做。

#函数参数
#位置参数：函数调用时，按照顺序传入参数，位置参数可以不按顺序传入。
#默认参数：函数调用时，可以不传入参数，使用默认参数。
#可变参数：函数调用时，可以传入任意数量的参数，参数类型为元组。
#关键字参数：函数调用时，可以传入任意数量的关键字参数，参数类型为字典。


#函数的定义
# def 函数名(参数列表):
#     函数体


#函数的调用
# 函数名(参数列表)   

#函数的返回值
# 函数名(参数列表)
# 函数的返回值 = 函数名(参数列表) 

#函数的注释
# 单行注释：# 注释内容
# 多行注释：''' 注释内容 ''' 或 """ 注释内容 """

#函数的命名规范
# 1. 函数名必须是见名知意的，能够准确描述函数的功能。
# 2. 函数名必须遵循驼峰命名法，即首字母小写，后续字母的首字母大写。
# 3. 函数名必须简短，一般不超过4个单词。
# 4. 函数名必须与变量名区分开，不要使用与关键字相同的名字。
# 5. 函数名应该避免使用缩写，除非是专业领域的缩写。 

#函数的测试
# 1. 函数的输入输出测试：测试函数的输入输出是否符合预期。
# 2. 函数的边界测试：测试函数的输入输出边界是否能正常运行。
# 3. 函数的异常测试：测试函数的输入输出异常是否能正常处理。
# 4. 函数的性能测试：测试函数的运行时间、内存占用等性能指标。
# 5. 函数的自动化测试：使用自动化工具对函数进行测试，如单元测试、集成测试、系统测试等。
