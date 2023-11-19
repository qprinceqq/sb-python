import time


def timeset_decorator(func):
    def timeset(*args, **kwargs):
        time.sleep(5)
        return func(*args, **kwargs)

    return timeset


@timeset_decorator
def print_func(text):
    print(str(text))


print('Выполнение функции...')
print_func('Привет!')
