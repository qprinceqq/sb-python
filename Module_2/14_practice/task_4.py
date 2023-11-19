def counter_decorator(func):


    def counter(*args, **kwargs):
        counter.calls += 1
        func(*args, **kwargs)
        print(f'Функция {func.__name__} была вызвана {counter.calls} раз')
    counter.calls = 0

    return counter


@counter_decorator
def say_hello():
    """
    Здесь есть документация! Ура!
    """
    print('Привет!')


for i in range(10):
    say_hello()
