def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    else:
        shangshu = a // b
        yushu = a % b
        return shangshu, yushu

print(divide(6, 3))#触发输出的是元组，一种无法编辑的列表

while True:
    choice = input("选择运算符号 (1【加】/2【减】/3【乘】/4【除】): ")
    if choice not in ["1", "2", "3", "4"]:
        print("没有此运算，请重新输入")
        continue
    else:
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))

        if choice == "1":
            print(add(num1, num2))

        elif choice == "2":
            print(subtract(num1, num2))

        elif choice == "3":
            print(multiply(num1, num2))

        elif choice == "4":      
            if num1/num2 == 0:
                print(f"{num1}/{num2}={divide(num1, num2)}")
            else:
                print(f"{num1}/{num2}={divide(num1, num2)[0]}余数是{divide(num1, num2)[1]}")

    choice = input("要在进行其他运算吗? (y/n): ")
    if choice.lower() != "y":#强制转换为小写字母
        print("再见")
        break