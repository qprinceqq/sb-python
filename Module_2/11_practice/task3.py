class Parent:
    def __init__(self, name, age, children):
        self.name = name  # str
        self.age = age  # int
        self.children = children  # Array of Child

    def info(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет. У меня {len(self.children)} детей.")

    def add_child(self, child):
        self.children.append(child)
        print(f"У {self.name} появился ребёнок: {child.name}. Поздраляем!")

    def calm_child(self, child):
        if child in self.children:
            child.state_of_calm = True
            print(f"{self.name} успокаивает {child.name}.")
        else:
            print(f"У {self.name} нет ребенка {child.name}")

    def feed_child(self, child):
        if child in self.children:
            child.state_of_hunger = False
            print(f"{self.name} кормит {child.name}.")
        else:
            print(f"У {self.name} нет ребенка {child.name}")


class Child:
    def __init__(self, name, age, state_of_calm, state_of_hunger):
        self.name = name  # str
        self.age = age  # int
        self.state_of_calm = state_of_calm  # boolian
        self.state_of_hunger = state_of_hunger  # boolian
