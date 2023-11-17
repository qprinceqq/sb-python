print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def nod(num_a, num_b):
  while num_a != num_b:
        if num_a > num_b:
          num_a -= num_b
        else:
          num_b -= num_a
  return num_b


print(f"Наибольший общий делитель  {nod(int(input('Введите первое число: ')), int(input('Введите второе число: ')))} ")