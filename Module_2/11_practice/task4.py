class Element:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Element):
            if (self.name, other.name) == ("Вода", "Воздух") or (self.name, other.name) == ("Воздух", "Вода"):
                return Storm()
            elif (self.name, other.name) == ("Вода", "Огонь") or (self.name, other.name) == ("Огонь", "Вода"):
                return Steam()
            elif (self.name, other.name) == ("Вода", "Земля") or (self.name, other.name) == ("Земля", "Вода"):
                return Mud()
            elif (self.name, other.name) == ("Огонь", "Воздух") or (self.name, other.name) == ("Воздух", "Огонь"):
                return Lightning()
            elif (self.name, other.name) == ("Земля", "Воздух") or (self.name, other.name) == ("Воздух", "Земля"):
                return Dust()
            elif (self.name, other.name) == ("Огонь", "Земля") or (self.name, other.name) == ("Земля", "Огонь"):
                return Lava()
            else:
                return None
        else:
            return None


class Water(Element):
    def __init__(self):
        super().__init__("Вода")


class Air(Element):
    def __init__(self):
        super().__init__("Воздух")


class Fire(Element):
    def __init__(self):
        super().__init__("Огонь")


class Earth(Element):
    def __init__(self):
        super().__init__("Земля")


class Storm(Element):
    def __init__(self):
        super().__init__("Шторм")


class Steam(Element):
    def __init__(self):
        super().__init__("Пар")


class Mud(Element):
    def __init__(self):
        super().__init__("Грязь")


class Lightning(Element):
    def __init__(self):
        super().__init__("Молния")


class Dust(Element):
    def __init__(self):
        super().__init__("Пыль")


class Lava(Element):
    def __init__(self):
        super().__init__("Лава")
