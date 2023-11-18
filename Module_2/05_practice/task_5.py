while True:
    password = input("Придумайте пароль: ")
    upper_chars = [char for char in password if char.isupper()]
    digit_chars = [char for char in password if char.isdigit()]
    if len(password) >= 8 and upper_chars != [] and digit_chars != []:
        print("Это надёжный пароль.")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")