import random

original_list = [random.randint(1, 10) for i in range(10)]
print("Оригинальный список:", original_list)
print("Новый список (способ 1):", [(original_list[i], original_list[i + 1]) for i in range(0, 10, 2)])

tuple_couple_list = []
for i in range(1, 11, 2):
    tuple_couple_list.append((original_list[i-1], original_list[i]))
print("Новый список (способ 2):", tuple_couple_list)
