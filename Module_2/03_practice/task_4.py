guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    choise = input("Гость пришёл или ушёл? ").upper()
    if choise == "ПОРА СПАТЬ":
        print("Вечеринка закончилась, все легли спать.")
        break

    guest_name = input("Имя гостя: ")
    if choise == "ПРИШЁЛ" or choise == "ПРИШЕЛ":
        if len(guests) == 6:
            print(f"Прости, {guest_name}, но мест нет")
        else:
            print(f"Привет, {guest_name}!")
            guests.append(guest_name)
    elif choise == "УШЁЛ" or choise == "УШЕЛ":
        if guest_name in guests:
            guests.remove(guest_name)
        else:
            print("Такого гостя нет")
    else:
        print("Неизвестная команда")

