def memoize_decorator(func):
    cache = {}

    def memoize(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    return memoize


@memoize_decorator
def fibonacci(n):
    """
    Здесь есть документация! Ура!
    Рекурсивная функция для вычисления чисел Фибоначчи.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 480
print(f"{n}-е число фибоначчи это: {fibonacci(n)}")
print(f"{n}-е число фибоначчи это: {fibonacci(n)}")
print(f"{n}-е число фибоначчи это: {fibonacci(n)}")
