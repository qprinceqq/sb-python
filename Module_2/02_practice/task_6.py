sdvig = int(input("Сдвиг: "))
numbers = list(map(int, input("Изначальный список (вводите через пробел): ").split()))
if sdvig > len(numbers): sdvig = sdvig % len(numbers)

print(f"Сдвинутый список: {[numbers[i-sdvig] for i in range(len(numbers))]}")
