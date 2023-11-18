while True:
    word_1 = input("Введите первую строку: ")
    word_2 = input("Введите вторую строку: ")
    if len(word_1) == len(word_2):
        break
    else:
        print("Строки разной длины, повторите ввод.")


for i in range(len(word_1)):
    if word_1 == word_2:
        print("Первая строка получается из второй со сдвигом", i)
        break
    word_2 = word_2[1:] + word_2[0]
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
