print('Задача 7. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input("Ввелите количество уровней пирамиды: "))
numblock = 1
for x in range(height):
  print("\t" * (height - x - 1), end = "")
  for i in range(x+1):
    print(numblock, end = "\t\t")
    numblock += 2

