print('Задача 6. Новоселье')

# Семья из трёх человек устала тесниться в однушке и наконец решила переехать.
# При обсуждении,
# какую же всё-таки купить квартиру исходя из своих предпочтений и семейного бюджета,
# они остановились на нескольких вариантах:

# Первый вариант 
# они готовы взять квартиру попросторнее (не менее 100 квадратных метров),
# но стоимостью не более 10 млн.
 
# Второй вариант — немного расширить круг поиска,
# то есть взять квартиру поменьше (от 80 квадратный метров),
# но и стоимостью не более 7 млн.
 
# Напишите программу,
# которая получает на вход стоимость квартиры и её площадь
# и выводит сообщение о том, подходит она или нет

square = float(input("Введите количество квадратных метров: "))
price = float(input("Введите стоимость квартиры в миллионах: "))
if square >= 100:
  if price <= 10:
    print("Квартира подходит!")
  else:
    print("Квартира не подходит =(")
elif square >= 80:
  if price <= 7:
    print("Квартира подходит!" + "\n")
  else:
    print("Квартира не подходит =(" + "\n")
else:
    print("Квартира не подходит =(" + "\n")