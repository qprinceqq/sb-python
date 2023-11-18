from random import uniform

list_1 = [round(uniform(5, 10), 2) for i in range(20)]
list_2 = [round(uniform(5, 10), 2) for i in range(20)]
list_winners = [max(list_1[i], list_2[i]) for i in range(20)]
print(f"Первая команда: {list_1}")
print(f"Вторая команда: {list_2}")
print(f"Победители тура: {list_winners}")
