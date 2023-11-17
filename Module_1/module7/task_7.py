print('Задача 7. Пропавшая карточка')

# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# 
# Вводится число N,
# далее еще N − 1 чисел: 
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

# Пример:
# Введите количество карточек: 5
# Введите номер оставшейся карточки: 1
# Введите номер оставшейся карточки: 4
# Введите номер оставшейся карточки: 5
# Введите номер оставшейся карточки: 3

# Номер пропавшей карточки: 2

n = int(input("Введите количество карточек: "))
orig_sum = sum(list(range(1, n + 1)))
our_sum = 0
for x in range(n - 1):
  our_sum += int(input("Введите номер оставшейся карточки: "))
print("Номер пропавшей карточки:", orig_sum - our_sum)