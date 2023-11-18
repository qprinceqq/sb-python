array_1 = {1, 5, 10, 20, 40, 80, 100}
array_2 = {6, 7, 20, 80, 100}
array_3 = {3, 4, 15, 20, 30, 70, 80, 120}

print("Задача 1:")
print("Решение с множествами:", array_1 & array_2 & array_3)

repeat_elements = []
for x in array_1:
    if x in array_2 and x in array_3:
        repeat_elements.append(x)
print("Решение без множеств:", repeat_elements)

print("Задача 2:")
print("Решение с множествами:", (array_1 - array_3) & (array_1 - array_2))
unique_elements = []
for x in array_1:
    if x not in array_2 and x not in array_3:
        unique_elements.append(x)
print("Решение без множеств:", unique_elements)

