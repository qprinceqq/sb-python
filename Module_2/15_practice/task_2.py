import math


class MyMath:
    @staticmethod
    def circumference_len(radius: float) -> float:
        """Вычисляет длину окружности."""
        return 2 * math.pi * radius

    @staticmethod
    def circle_area(radius: float) -> float:
        """Вычисляет площадь окружности."""
        return math.pi * radius ** 2

    @staticmethod
    def cube_volume(side: float) -> float:
        """Вычисляет объем куба."""
        return side ** 3

    @staticmethod
    def sphere_surface_area(radius: float) -> float:
        """Вычисляет площадь поверхности сферы."""
        return 4 * math.pi * radius ** 2


print("Длина окружности радиуса 6:", MyMath.circumference_len(6))
print("Площадь окружности радиуса 6:", MyMath.circle_area(6))
print("Объем куба стороной 6:", MyMath.cube_volume(6))
print("Площадь поверхности сферы радиуса 6:", MyMath.sphere_surface_area(6))
