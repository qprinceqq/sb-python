from collections import Counter


def may_polindrom(word):
    char_count_dict = Counter(word)
    odd_count = 0
    for quantity in char_count_dict.values():
        if quantity % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return "Нельзя сделать палиндромом."
    return "Можно сделать палиндромом."


print(may_polindrom(input("Введите строку: ")))
