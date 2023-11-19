
username = input("Введите ваше имя или никнейм: ")
while True:
    print('   1 - Посмотреть текущий текст чата.'
          '\n   2 - Отправить сообщение.'
          '\n   3 - Выйти из чата.\n')
    choice = int(input('Выберите действие: '))
    if choice == 1:
        with open('history_chat.txt', 'r', encoding='utf-8') as chat_file:
            print(f'\nТекущий текст чата:\n{chat_file.read()}')

    elif choice == 2:
        with open('history_chat.txt', 'a', encoding='utf-8') as chat_file:
            user_message = input('  > ')
            if user_message.strip() == '':
                print('Сообщение не может быть пустой строкой!')
            else:
                chat_file.write(f'{username}: {user_message}\n')
    elif choice == 3:
        break
    else:
        print('Ошибка! Выберите одно из доступных действий.')
