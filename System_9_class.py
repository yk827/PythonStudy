import random

class Player_default:
    hp = 100
    attackCount = 30
    def __init__(self, name=None, profession=None):
        self.name = name
        self.profession = profession

    def defense(self, option):
        if option == 1:
            print(f"{self.name} 使用防御！")
            return 0.5
        elif option == 2:
            print(f"{self.name} 使用闪避！")
            return random.choice([0.2,1])

class Player_soldier(Player_default):
    def attack(self, option):
        if option == 1:
            print(f"{self.name} 使用突刺攻击了敌人，造成了{self.attackCount}点伤害！")
            return self.attackCount

        elif option == 2:
            print(f"{self.name} 使用斩击攻击了敌人，造成了{self.attackCount*2}点伤害！")
            return random.choice([self.attackCount, self.attackCount*2])

class Player_enermy(Player_default):
    def attack(self, option):
        if option == 1:
            print(f"{self.name} 使用挥砍攻击了敌人，造成了{self.attackCount}点伤害！")
            return self.attackCount

        elif option == 2:
            print(f"{self.name} 使用偷袭攻击了敌人，造成了{self.attackCount*3}点伤害！")
            return random.choice([self.attackCount, self.attackCount*3])

Player_a = Player_soldier(input("请输入你的名字："), input("请输入你的职业："))
Player_b = Player_enermy(input("请输入你的名字："), input("请输入你的职业："))

print(f"玩家{Player_a.name}的职业是{Player_a.profession}！")
print(f"玩家{Player_b.name}的职业是{Player_b.profession}！")

random_enemyChoice = random.choice([1,2])

while True:
    attack_option = input("请输入你的攻击选项1(突刺)2(斩击)：")
    if attack_option not in ['1', '2']:
        print("无效的选项，请重新输入！")
        continue
    Player_a_attackAccount = Player_a.attack(attack_option)
    print(Player_a_attackAccount)  # 调试信息，确保攻击值正确
    enermy_hp = int(Player_b.defense(random_enemyChoice) * Player_a_attackAccount)
    Player_b.hp -= enermy_hp
    if Player_b.hp <= 0:
        print(f"玩家{Player_b.name}被击败了！")
        break
    else:
        print(f"玩家{Player_b.name}的剩余血量为{Player_b.hp}！")
        print(f"玩家{Player_a.name}的剩余血量为{Player_a.hp}！")
        print("")

    defense_option = input("请输入你的防御选项1(防御)2(闪避)：")
    Player_b_attackAccount = Player_b.attack(random_enemyChoice)

    soldier_hp = int(Player_a.defense(defense_option)*Player_b_attackAccount)
    Player_a.hp -= soldier_hp
    if Player_a.hp <= 0:
        print(f"玩家{Player_a.name}被击败了！")
        break
    else:
        print(f"玩家{Player_b.name}的剩余血量为{Player_b.hp}！")
        print(f"玩家{Player_a.name}的剩余血量为{Player_a.hp}！")
        print("")