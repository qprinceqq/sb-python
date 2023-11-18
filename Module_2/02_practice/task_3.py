list_vcards = []
for i in range(int(input("Введите кол-во видеокарт: "))):
    list_vcards.append(int(input(f"Видеокарта {i+1}: ")))

max_card = max(list_vcards)
print(list(filter(lambda x: x != max_card, list_vcards)))
