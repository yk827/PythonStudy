list1 = [1, 2, 3, 4, 5]
for i in list1:
    if i == 3:  # if i is equal to 3, break out of the loop
        break
    print(i)    # print the current value of i

print("After the loop1")

# The continue statement is used to skip the current iteration and move to the next one.
for i in list1:
    if i == 3:
        continue  # skip the current iteration and move to the next one
    print(i)
#print("After the loop2")

#for i in list:
#   for j in range(1, 4):  # iterate over the range 1 to 3
#       print(i * j)  # print the product of i and j
#  print(i)

print("After the loop3")
list2 = ["bulin.py", 2, 3, 4, 5]
print(list2)
for i in list2:
    if type(i) == int:  # if i is an integer, skip it
        continue
    print(i)  # print the current value of i


#开一套新的循环案例

breakfast_mains = ["eggs", "bacon", "toast", "coffee"]
breakfast_desserts = ["cake", "ice cream", "pudding"] 
count = 0
for main in breakfast_mains:
    for dessert in breakfast_desserts:
        print(main + " and " + dessert)
        count += 1
print(f"总共有{count}种套餐组合")

# 筛选数列
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num%3 == 0:
        even_numbers.append(num)
print(f"被3整除的数列为{even_numbers}")


#range()函数的用法
n = 0
for i in range(3, 11, 3):
    n += 1
    print(f"第{n}次循环，i的值为{i}")


# 利用range()函数实现斐波那契数列
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a+b    # 计算下一个数 

 
# 利用列表推导式实现斐波那契数列
fibonacci = [0, 1]
print(fibonacci)     # [0, 1]
for i in range(2, 10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(fibonacci)     # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]   

# 利用列表推导式实现素数
primes = [2]
for i in range(3, 100):
    is_prime = True
    for j in range(2, int(i**0.5)+1):    # 优化，只检查i的开平方以内的数
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print(primes)     #检测的数字只能是i的平方之内能整除的数，超过i的平方的数也可能有因数不一定是素数

# 利用列表推导式实现阶乘
factorial = 1
for i in range(1, 6):
    factorial *= i
print(factorial)   