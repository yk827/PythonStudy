correct_password = "password"
for i in range(3):
    password = input("请输入密码: ")
    if password == correct_password:
        print("登录成功")
        break
    else:
        print(f"密码错误，请重新输入，您还剩余{2-i}次机会")

else:
    print("账号已被锁定")  