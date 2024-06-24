meat = 100
fish  = 75
chicken = 20

print(meat>fish)
print(type(meat>fish))

print(meat == chicken)
print(meat != fish)
print(not chicken != fish)

print(meat == chicken and meat != fish)
print(meat == chicken or meat != fish)

if  meat>fish:
    print("meat更贵")
else:
    print("fish更贵")


#upper的作用是把输入的文本转化为大写字母
dish = input("你想要吃什么（A）猪肉？（B）鱼肉？").upper()
if dish == 'A':
    print("猪肉的价格是" + str(meat))
else:
    print("鱼肉的价格是" + str(fish))




#if判断的嵌套
dishgroup = input("是否升级套餐（Y）是？（N）不要？").upper()
if dish == 'A':
    if dishgroup == "Y":
        print("套餐总价格是" + str(meat+chicken))
    else:
        print("猪肉的价格是" + str(meat))
else:
    if dishgroup == "Y":
        print("套餐总价格是" + str(fish + chicken))
    else:
        print("鱼肉的价格是" + str(fish))

#换一种elif写法
print("开始第二次点餐")
if dish == "A" and dishgroup == "Y":
    print(f"套餐的总价格是{meat+chicken}")
elif dish == "A" and dishgroup == "N":
    print(f"套餐的总价格是{meat}")
elif dish == "B" and dishgroup == "Y":
    print(f"套餐的总价格是{fish+chicken}")
else:
    print(f"套餐的总价格是{fish}")