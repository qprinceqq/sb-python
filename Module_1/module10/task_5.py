print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

n = int(input("Введите количество чисел: "))
max_sum = 0
max_ind = 0
sum = 0
for x in range(n):
  num = int(input(f"{x+1}. Введите число: "))
  for i in str(num):
    sum += int(i)
  if sum > max_sum:
    max_sum = sum
    max_ind = x
  sum = 0
print(f"Наибольшая сумма цифр {max_sum} у числа номер {max_ind+1}")