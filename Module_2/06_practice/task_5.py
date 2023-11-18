synonyms = {}
for i in range(int(input("Введите количество пар слов: "))):
    word_1, word_2 = input(f"{i + 1}-я пара слов (через '-'): ").lower().replace(" ", "").split("-")
    synonyms[word_1] = word_2

tip = True
while tip:
    word = input("Введите слово: ").lower()
    for couple in synonyms.items():
        if word == couple[0]:
            print("Синоним:", couple[1])
            tip = False
            break
        elif word == couple[1]:
            print("Синоним:", couple[0])
            tip = False
            break
    else:
        print("Такого слова в словаре нет.")
