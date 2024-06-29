class Player_default:
    level_default = 1
    exp_default = 0
    gold_default = 100
    def __init__(self, name=None, birth=None): #定义构造函数，初始化属性，并传入参数，init方法是类的初始化方法，在创建对象时自动调用。self代表类的实例。
#self代表目前在建立的角色对象，name和birth是参数，分别代表角色的名字和出生日期。
        self.name = name
        self.birth = birth
    
    def move(self):
        print(self.name + "正在移动...")
    
    def attack(self, target):
        print(self.name + "正在攻击" + target.name + "...")

Player1 = Player_default()
Player2 = Player_default()

Player1.name = str(input("请输入Player1的名字："))
Player1.birth = str(input("请输入Player1的出生日期："))
Player2.name = str(input("请输入Player2的名字："))
Player2.birth = str(input("请输入Player2的出生日期："))

Player1.move()
Player2.move()

Player1.attack(Player2)
Player2.attack(Player1)

print("Player1的属性：", Player1.__dict__)
print("Player2的属性：", Player2.__dict__)


class Soldier_default(Player_default):
    def defense(self, target):
        print(f"{self.name}+ '正在防御' + {target.name} + '...'")
        return f"{self.name}防御了{target.name}！"

Player3 = Soldier_default()
Player3.name = str(input("请输入Player3的名字："))
Player3.birth = str(input("请输入Player3的出生日期："))

Player3.move()

Player3.attack(Player2)
print(Player3.defense(Player2))
print(Player3.__dict__)