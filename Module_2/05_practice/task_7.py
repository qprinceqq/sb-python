def func(ip_splited):
    if len(ip_splited) == 4:
        for i in ip_splited:
            if not (i.isalnum() and i.isdigit()):
                return f"{i} - это не целое число."

        for numbers in ip_splited:
            if int(numbers) > 255:
                return f"{numbers} превышает 255."

        return "IP-адрес корректен."
    else:
        return "Адрес — это четыре числа, разделённые точками."


print(func(input("Введите IP: ").split(".")))
