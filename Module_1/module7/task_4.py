print('Задача 4. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

grades = map(int, input("Введите все оценки класса через пробел: ").split())
a = 0
b = 0
c = 0
for x in grades:
  if x == 5:
    a += 1
  elif x == 4:
    b += 1
  elif x == 3:
    c += 1
if a > b and a > c:
  print(f"Сегодня больше отличников, их {a}")
elif b > a and b > c:
  print(f"Сегодня больше хорошистов, их {b}")
elif c > a and c > b:
  print(f"Сегодня больше троечников, их {c}")
else:
  print("Да хз блин")
