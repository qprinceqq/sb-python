print('Задача 8. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.
 
# Напишите программу, 
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
 
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: При желании найдите описание алгоритма бинарного поиска и попробуйте применить в этой задаче.
#Разбор подобного решения будет в следующем модуле.


n = 50
step = 25
trycount = 0
tip = 0
while True:
  trycount += 1
  print("Твое число равно, меньше или больше, чем число", n, "?")
  tip = int(input("1 - равно, 2 - больше, 3 - меньше: "))
  
  if tip == 2:
    n += step
  elif tip == 3:
    n -= step
  elif tip == 1:
    break
    
  if step != 1:
    step //= 2
  if trycount == 4: 
    step += 1
  if n == 100 or n == 1:
    break
    
print("Программа угадала ваше число -", n)
print("Количество попыток -", trycount)