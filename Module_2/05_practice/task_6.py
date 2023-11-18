string = input("Введите строку: ")
new_string = ""
count = 1
for i in range(len(string)):
    if (i != len(string) - 1) and string[i] == string[i+1]:
        count += 1
    else:
        new_string += string[i] + str(count)
        count = 1

print("Закодированная строка:", new_string)