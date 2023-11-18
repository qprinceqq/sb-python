orders = {}
for i in range(int(input("Введите количество заказов: "))):
    order_name, pizza_name, quantity = input(f"{i+1}-й заказ: ").split()
    quantity = int(quantity)
    if order_name in orders:
        if pizza_name in orders[order_name]:
            orders[order_name][pizza_name] += quantity
        else:
            orders[order_name][pizza_name] = quantity
    else:
        orders[order_name] = {pizza_name: quantity}

print("Итоговый заказ:")
for key in orders.keys():
    print(f"{key}: ")
    for order in orders[key]:
        print(f"{order} : {orders[key][order]}")

