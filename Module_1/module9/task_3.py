print('Задача 3. Театр')

# В городе планируют построить театр под открытым небом, но для начала нужно оценить, сколько сделать рядов, сидений в них и каким должно быть расстояние между рядами.

# Что нужно сделать

# Напишите программу, которая получает на вход количество рядов, сидений и свободных метров между рядами, а затем выводит примерный макет театра на экран.

# Сцена
# Введите кол-во рядов: 5
# Введите кол-во сидений ряду: 7
# Введите кол-во метров между рядами: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======

row = int(input("Введите кол-во рядов: "))
seat = int(input("Введите кол-во сидений ряду: "))
distance = int(input("Введите кол-во метров между рядами: "))
print("")
for x in range(row):
  print("=" * seat + " " + distance*"*" + " " + seat*"=")

