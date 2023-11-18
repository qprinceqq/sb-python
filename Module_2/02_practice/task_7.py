word = input("Введите слово: ")
if "".join([word[-i - 1] for i in range(len(word))]) == word:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
