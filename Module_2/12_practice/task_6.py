from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius ** 2, 4)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return round(self.width * self.height, 4)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return round(self.base * self.height / 2.0, 4)


print("Площадь круга радуса 7:", Circle(7).area())
print("Площадь прямоугольника 5 на 12:", Rectangle(5, 12).area())
print("Площадь треугольника с основанием 5 и высотой 12:", Triangle(5, 12).area())
