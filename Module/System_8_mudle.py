#模块的导入方式：
#1. import 模块名
#2. from 模块名 import 变量名
#3. from 模块名 import 函数名
#4. from 模块名 import *
#5. import 模块名 as 别名
#6. from 模块名 import 变量名 as 别名
#7. from 模块名 import 函数名 as 别名
#8. from 模块名 import * as 别名
#9. import 模块名.变量名
#10. from 模块名.变量名 import 变量名
#11. from 模块名.变量名 import 函数名
#12. from 模块名.变量名 import *
#13. import 模块名.变量名 as 别名
#14. from 模块名.变量名 import 变量名 as 别名
#15. from 模块名.变量名 import 函数名 as 别名
#16. from 模块名.变量名 import * as 别名

import Study_8_mudle
add = Study_8_mudle.add
print(add(1, 1))

from Study_8_mudle import add
print(add(2, 2))

from Study_8_mudle import *
print(add(3, 3))

import Study_8_mudle as sm
print(sm.add(4, 4))

from Study_8_mudle import add as a
print(a(5, 5))

'''import Study_8_mudle.add
print(add(7, 7))'''

'''from Study_8_mudle.add import add
print(add(8, 8))'''

'''from Study_8_mudle.add import *
print(add(9, 9))'''

'''import Study_8_mudle.add as sa
print(sa(10, 10))'''

'''from Study_8_mudle.add import add as a
print(a(11, 11))'''


# 注意：
# 1. 模块名必须是存在的，否则会报错；
# 2. 模块名和变量名之间用点“.”分隔，表示从某个模块中导入变量或函数；
# 3. 导入模块时，可以用as给模块起别名，方便使用；
# 4. 导入模块时，可以用*来导入模块中的所有变量或函数，但不推荐；
# 5. 导入模块时，如果模块中有同名变量或函数，则导入的变量或函数会覆盖原有同名变量或函数；



import random
s = "hello world"
letter = [1, 2, 3, 4, 5]
random.shuffle(letter)
print(letter)

x = random.randint(1, 10)
print(x)

y = random.random()
print(y)

z = random.choice(letter)
print(z)

#random.seed() 函数用于初始化随机数生成器，以确保随机数的生成是可重复的。通过设置相同的种子值，可以使得随机数生成器在每次运行时生成相同的随机数序列。
# 如果没有设置种子值，则每次运行时，随机数生成器都会生成不同的随机数序列。这在需要重现随机结果的场景中非常有用，例如在调试或测试过程中。
random.seed(s)
print(random.random())