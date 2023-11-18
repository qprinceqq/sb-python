numbers = []
for i in range(int(input("Количество чисел: "))):
    numbers.append(int(input("Число: ")))
print(f"Последовательность: {numbers}")

for i in range(len(numbers)):
    try_polindrom = numbers[i:]
    if try_polindrom == try_polindrom[::-1]:
        print("Нужно приписать чисел: ", i)
        print("Сами числа: ", numbers[:i][::-1])
        break


