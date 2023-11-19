class Property:
    def __init__(self, worth):
        self.worth = worth

    def get_taxes(self, other):
        return 0


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def get_taxes(self):
        return self.worth / 1000.0


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def get_taxes(self):
        return self.worth / 200.0


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def get_taxes(self):
        return self.worth / 500.0


money = float(input("Введите количество ваших денег: "))
worth = float(input("Введите стоимость вашего имущества: "))

apartment = Apartment(worth)
car = Car(worth)
country_house = CountryHouse(worth)

print(f"Налог на квартиру: {apartment.get_taxes()}")
print(f"Налог на машину: {car.get_taxes()}")
print(f"Налог на дачу: {country_house.get_taxes()}")
in_total = apartment.get_taxes() + car.get_taxes() + country_house.get_taxes()
print(f"Общий налог: {in_total}")

if money >= in_total:
    print("У вас достаточно денег для уплаты налогов")
else:
    print(f"Вам не хватает {in_total - money} денег для уплаты налогов")
