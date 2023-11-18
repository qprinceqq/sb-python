def to_add(contacts):
    name, surname = input("Введите имя и фамилию нового контакта (через пробел): ").split()
    if (name, surname) in contacts:
        print("Такой человек уже есть в контактах.")
        return
    else:
        phone = input("Введите номер телефона: ")
        contacts[(name, surname)] = phone


def to_find(surname_to_find):
    found_contacts = {f"{name} {surname}": phone for (name, surname), phone in contacts.items() if
                      surname.lower() == surname_to_find.lower()}
    if found_contacts:
        for contact, phone in found_contacts.items():
            print(contact, phone)
    else:
        print("Контакт с такой фамилией не найден.")


contacts = {}
while True:
    try:
        act = int(input("Введите номер действия: \n(1 - добавить контакт, 2 - найти человека) "))
        if act == 1:
            to_add(contacts)
            print("Текущий словарь контактов:", contacts)
        elif act == 2:
            to_find(input("Введите фамилию для поиска: "))
    except:
        print("Некорректное действие. Попробуйте снова.")
