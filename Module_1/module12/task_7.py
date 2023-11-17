print('Задача 7. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

from random import randint

def rock_paper_scissors():
  player = input("Камень, ножницы или бумага? ").lower()
  computer = ("Камень", "Ножницы", "бумага")[randint(0, 3)]
  if computer == "Камень":
    if player == "камень":
      print("Ничья, компьютер выбрал камень")
    elif player == "ножницы":
      print("Вы проиграли, компьютер выбрал камень")
    elif player == "бумага":
      print("Вы выиграли, компьютер выбрал камень")
  elif computer == "Ножницы":
    if player == "камень":
      print("Вы выиграли, компьютер выбрал ножницы")
    elif player == "ножницы":
      print("Ничья, компьютер выбрал ножницы")
    elif player == "бумага":
      print("Вы проиграли, компьютер выбрал ножницы")
  else:
    if player == "камень":
      print("Вы проиграли, компьютер выбрал бумагу")
    elif player == "ножницы":
      print("Вы выиграли, компьютер выбрал бумагу")
    elif player == "бумага":
      print("Ничья, компьютер выбрал бумагу")


def guess_the_number():
  quizznum = randint(1, 300)
  print("Программа загадала число от 1 до 300, попробуйте его отгадать!")
  trycount = 0
  while True:
    trynum = int(input("Введите число: "))
    trycount += 1
    if trynum > quizznum:
      print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif trynum < quizznum:
      print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
      print(f"Вы угадали! Число попыток: {trycount}, Загаданное число {quizznum}.")
      break


def mainMenu():
  print("1 - Камень, ножницы, бумага \n2 - Угадай число")
  n = int(input("Во что будете играть? "))
  if n == 1:
    rock_paper_scissors()
  if n == 2:
    guess_the_number()

mainMenu()