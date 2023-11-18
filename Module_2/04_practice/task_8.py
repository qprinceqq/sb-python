cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
crypt_message = ""
message = input("Введите сообщение: ").lower()
sdvig = int(input("Введите сдвиг: "))
sdvig = sdvig % 33

for i in message:
    if i not in cyrillic:
        crypt_message += i
    else:
        crypt_message += cyrillic[(cyrillic.index(i) + sdvig) % 33]

print(f"Зашифрованное сообщение: {crypt_message}")
