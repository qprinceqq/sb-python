import math


def get_sqrt(number):
    if number < 0:
        raise ValueError("Нельзя взять корень из отрицательного числа")
    if number == 0:
        raise ValueError("Нельзя взять корень из нуля")

    return math.sqrt(number)


try:
    num = float(input("Введите число: "))
    print(f"Квадратный корень числа {num} равен {round(get_sqrt(num), 4)}")
except Exception as error:
    print(f"Ошибка! {error}")
