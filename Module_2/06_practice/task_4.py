original_dict = {}
fixed_dict = {}

for char in input("Введите текст: "):
    if char in original_dict:
        original_dict[char] += 1
    else:
        original_dict[char] = 1

print("Оригинальный словарь частот: ")
for char in original_dict:
    print(f'{char} : {original_dict[char]}')

for char in original_dict.keys():
    if original_dict[char] in fixed_dict:
        fixed_dict[original_dict[char]].append(char)
    else:
        fixed_dict[original_dict[char]] = [char]

print("Инвертированный словарь частот:")
for num in fixed_dict.keys():
    print(f'{num} : {fixed_dict[num]}')
