print('Задача 2. Функция в функции')

# Евгений проходит специальный тест по программированию.
# У него всё шло хорошо, пока он не наткнулся на тему “Функции”.
# 
# Задание звучит так:
# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода.
# 
# Это вызов функции test().
# В ней запрашивается на ввод целое число.
# Если оно положительное, то вызывается функция positive(),
# тело которой содержит команду вывода на экран слова "Положительное".
# 
# Если число отрицательное, то вызывается функция negative(),
# ее тело содержит выражение вывода на экран слова "Отрицательное".
# 
# Помогите Евгению и реализуйте такую программ


def positive():
  print("Положительное")


def negative():
  print("Отрицательное")


def test():
  n = int(input("Введите число: "))
  if n >= 0:
    positive()
  elif n < 0:
    negative()
    

test()