print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
# 
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
# 
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
# 
# Пример 1:
# 
# Введитечисло: 92345
# 
# Формат плавающей точки: x = 9.2345 * 10 ** 4
# 
# Пример 2:
# 
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3


n = input("Введите число: ")
count = 0
for x in n:
  count += 1
  if x != "0" and x != ".":
    if float(n) >= 1:
      res = x + "." + n[count:] +  " * 10 ** " + str(len(n[count:]))

    else:
      res = x + "." + n[count:] + " * 10 ** -" + str(count-2)
    print(res)
    break
