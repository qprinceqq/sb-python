print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула: 
# S = ab/2

a, b = int(input('Введите длину 1-го катета: ')), int(input('Введите длину 2-го катета: '))
print("Площадь", a * b * 0.5)

