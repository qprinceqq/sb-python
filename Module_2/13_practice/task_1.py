class ClassIterator:
    def __init__(self, n):
        self.N = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.N:
            to_return = self.i ** 2
            self.i += 1
            return to_return
        else:
            raise StopIteration


def squares_generator(N):
    i = 1
    while i <= N:
        yield i ** 2
        i += 1




n = int(input("Введите число N: "))

for x in ClassIterator(n):
    print("Класс-итератор:", x)

for x in squares_generator(n):
    print("Функция-генератор:", x)

for x in ((i + 1) ** 2 for i in range(n)):
    print("Генераторное выражение:", x)
