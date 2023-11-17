print('Задача 5. Функция')

# Перед изучением функций из программирования Саша решил оживить свои знания о функциях математики. Помогите Саше написать программу, которая будет считать значение функции в каждой точке отрезка с нужным шагом, начиная с конца).
# Напишите программу, которая получает на вход начало и конец отрезка, а также шаг (отрицательный), а затем высчитывает функцию y в каждой точке отрезка и выводит ответ на экран с нужным шагом, начиная с конца.

# Сама функция выглядит так:
# y = x**3 + 2*x**2 - 4*x + 1

# Пример:
# 
# Введите начало отрезка: -2
# Введите конец отрезка: 2
# Введите шаг: -1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке -1 функция равна 6
# В точке -2 функция равна 9

start = int(input("Введите начало отрезка: "))
end = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг(отрицательный): "))
for x in range(end, start - 1, step):
  y = x**3 + 2*x**2 - 4*x + 1
  print(f"В точке {x} функция равна {y}")
