print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы 
# и любой цифры в тексте (а не только буквы Ы как раньше).
# 
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
# 
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
# 
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
# 
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(text, n, sign):
  count_n = 0
  count_sign = 0
  for symbol in text:
    if symbol == n:
      count_n += 1
    elif symbol == sign:
      count_sign += 1
      
  print(f"Количество цифр {n}: {count_n}")
  print(f"Количество букв {sign}: {count_sign}")


text = input("Введите текст: ")
num = input("Какую цифру ищем? ")
sign = input("Какую букву ищем? ")
count_letters(text, num, sign)