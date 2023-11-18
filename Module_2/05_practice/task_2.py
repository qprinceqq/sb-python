words = input("Введите строку: ").replace(".", "").split()
len_list = [len(word) for word in words]
max_len = max(len_list)
print(f'Самое длинное слово: "{words[len_list.index(max_len)]}".')
print(f"Длина этого слова: {max_len}.")

