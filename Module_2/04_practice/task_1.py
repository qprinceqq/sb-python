res = []
find = "ауоыиэяюёе"
for char in input("Введите текст: "):
    if char.lower() in find:
        res.append(char)

print(f"Список гласных букв: {res}")
print(f"Длина списка: {len(res)}")
