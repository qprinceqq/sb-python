print('Задача 6. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######

height = int(input("Введите высоту пирамиды: "))
for x in range(height):
  print((height-x-1) * " " + (2*x+1) * "#")
