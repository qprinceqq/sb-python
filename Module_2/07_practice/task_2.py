def is_prime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, round(number ** 0.5 + 1)):
        if number % i == 0:
            return False
    return True


def crypto(obj):
    obj = list(enumerate(obj))
    return [obj[i][1] for i in range(obj[-1][0]) if is_prime(i)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
