group = list(range(1, int(input("Количество человек: ")) + 1))
sdvig = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {sdvig}-й человек", end="\n\n")

del_index = 0
for i in range(len(group)-1):
    print(f"Текущий круг людей: {group}")
    print(f"Начало счёта с номера {group[del_index % len(group)]}")
    del_index = (del_index + sdvig - 1) % len(group)
    print(f"Выбывает человек под номером {group[del_index]}", end="\n\n")
    group.pop(del_index)

print(f"Остался человек под номером {group[0]}")