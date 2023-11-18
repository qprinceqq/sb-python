shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
price = 0
while True:
    detail_name = input("Название детали: ")
    fixed_list = list(filter(lambda x: x[0] == detail_name, shop))
    if len(fixed_list) >= 1:
        break
    print("Такой детали у нас нет")
print(f"Количество деталей: {len(fixed_list)}")
print(f"Общая стоимость: {sum(list(map(lambda x: x[1], fixed_list)))}")





