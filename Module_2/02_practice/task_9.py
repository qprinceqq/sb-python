test = list(map(int, input("Изначальный список (вводите через пробел): ").split()))
print(list(filter(lambda i: i % 2 == 0, [test[-i-1] for i in range(len(test))])))
