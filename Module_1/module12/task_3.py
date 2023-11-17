print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия. 
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру. 

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.


def sum_numeral(num):
  sum = 0
  while num > 0:
    sum += num % 10
    num //= 10
  print(f"Сумма цифр равна {sum}")


def max_numeral(num):
  maxnum = 0
  while num > 0:
    if maxnum < num % 10:
      maxnum = num % 10
    num //= 10
  print(f"Наибольшая цифра {maxnum}")


def min_numeral(num):
  minnum = 10
  while num > 0:
    if minnum > num % 10:
      minnum = num % 10
    num //= 10
  print(f"Наименьшая цифра {minnum}")


print("1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра, 0 - покинуть программу")
while True:
  num = int(input("Введите число: "))
  choise = int(input("Введите действие: "))
  if choise == 1:
    sum_numeral(num)
  elif choise == 2:
    max_numeral(num)
  elif choise == 3:
    min_numeral(num)
  elif choise == 0:
    break