import random


def get_killed():
    if random.randint(1, 13) == 1:
        raise Exception('Вас постигла неудача!')


with open('out_file.txt', 'w') as file:
    file.write("")

with open('out_file.txt', 'a') as file:
    summa = 0
    while summa < 777:
        user_input = int(input('Введите число: '))
        get_killed()
        file.write(str(user_input) + '\n')
        summa += user_input

    print('Вы успешно выполнили условие для выхода из порочного цикла!')
