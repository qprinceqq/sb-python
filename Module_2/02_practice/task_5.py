while True:
    num = int(input("Количество контейнеров: "))
    if num <= 200:
        break

containers = []
for i in range(num):
    while True:
        container_weight = int(input("Введите вес контейнера: "))
        if container_weight <= 200:
            containers.append(container_weight)
            break
new_container = int(input("Введите вес нового контейнера: "))

containers.sort(reverse=True)
for i in range(len(containers)):
    if containers[i] < new_container:
        i -=1
        break

print(f"Номер, который получит новый контейнер: {i + 2}")
