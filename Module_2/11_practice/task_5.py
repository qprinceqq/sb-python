import random


class Human:
    def __init__(self, name, home):
        self.name = name
        self.satiety = 50
        self.home = home

    def get_info(self):
        print(f"Меня зовут {self.name}, моя сытость {self.satiety}")

    def eat(self):
        self.satiety += 10
        self.home.food -= 10

    def go_work(self):
        self.satiety -= 10
        self.home.money += 50

    def play(self):
        self.satiety -= 20

    def go_shopping(self):
        self.home.food += 50
        self.home.money -= 50

    def live_day(self):
        dice = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.home.food < 10:
            self.go_shopping()
        elif self.home.money < 50:
            self.go_work()
        elif dice == 1:
            self.go_work()
        elif dice == 2:
            self.eat()
        else:
            self.play()


class Home:
    def __init__(self):
        self.food = 50
        self.money = 0

    def get_info(self):
        print(f"Еды дома - {self.food}, Денег дома - {self.money}")


home = Home()
person1 = Human("Дима", home)
person2 = Human("Рахмет", home)

for i in range(365):
    person1.live_day()
    person2.live_day()
    person1.get_info()
    person2.get_info()
    home.get_info()
    print("")
