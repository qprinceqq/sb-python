size_list = []
count = 0
for i in range(int(input("Количество роликов: "))):
    size = input(f"Размер пары {i+1}: ")
    size_list.append(size)

for i in range(int(input("Количество людей: "))):
    foot = input(f"Размер ноги человека {i+1}: ")
    try:
        size_list.remove(foot)
        count += 1
    except:
        pass

print(f"Наибольшее количество людей, которые могут взять ролики: {count}")