import datetime


def logging_decorator(func):
    def logging(*args, **kwargs):
        try:
            print(f'Название функции: {func.__name__}')
            print(f'Документация функции: {func.__doc__}')
            func(*args, **kwargs)
        except Exception as e:
            with open('function_errors.log', 'w', encoding="utf-8") as file:
                file.write(f'{datetime.datetime.now()}, {func.__name__}: {str(e)}\n')

    return logging


def func():
    """
    Это документация.
    """
    print('Привет!')
    print(1 / 0)


logging_decorator(func)()
