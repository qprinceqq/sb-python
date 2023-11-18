def count_uppercase_lowercase(text):
    upper_count = sum([1 for char in text if char.isupper()])
    lower_count = sum([1 for char in text if char.islower()])
    return upper_count, lower_count


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
