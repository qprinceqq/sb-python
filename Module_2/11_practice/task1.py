import random


class Warrior:
    hp = 100
    name = "Воин"

    def take_damage(self):
        self.hp -= 20
        print(f"Оставшееся здоровье: {self.hp}")


unit_1 = Warrior()
unit_2 = Warrior()
while unit_1.hp != 0 and unit_2.hp != 0:
    if bool(random.getrandbits(1)):
        print("Атаковал unit_1:")
        print("2. ", end="")
        unit_2.take_damage()
    else:
        print("Атаковал unit_2:")
        print("1. ", end="")
        unit_1.take_damage()

if unit_1.hp > unit_2.hp:
    print("Победу одержал unit_1")
else:
    print("Победу одержал unit_2")
