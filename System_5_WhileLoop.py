price = 1000
A=input("输入第一位玩家名字：")
B=input("输入第二位玩家名字：")
# i = 3

def Price_game(i):
    while i >= 1:
        i-=1
        A_money = int(input(f"请玩家{A}输入金额"))
        B_money = int(input(f"请玩家{B}输入金额"))
        if i >= 1:
            if A_money == price and B_money == price:
                print("平局")
                break
            elif B_money ==price:
                print(f"玩家{B}胜利")
                break
            elif A_money ==price:
                print(f"玩家{A}胜利")
                break
            else:
                print(f"玩家游戏继续,剩余{i}轮")
               # continue
        else:
            print("游戏结束")
            break
    print("欢迎再次参赛")


#另一种规则
while True:
    A_money = int(input(f"请玩家{A}输入金额"))
    B_money = int(input(f"请玩家{B}输入金额"))
    if A_money == price and B_money == price:
        print("平局")
        break
    elif B_money ==price:
        print(f"玩家{B}胜利")
        break
    elif A_money ==price:
        print(f"玩家{A}胜利")
        break
    elif abs(A_money-price)<abs(B_money-price):
        print(f"玩家{A}胜利")
        break
    else:
        print(f"玩家{B}胜利")
        break
print("欢迎再次参赛")