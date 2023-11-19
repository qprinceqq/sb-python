from datetime import datetime
import time


def sub_log(my_class, func, format):
    """Декоратор для логирования методов класса."""
    def into(*args, **kwargs):
        print(f'Запускается "{my_class.__name__}.{func.__name__}"', end=". ")
        print(f'Дата и время запуска: {datetime.now().strftime(format)}')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f'Завершение "{my_class.__name__}.{func.__name__}"', end=", ")
        print(f'время работы = {round(end, 3)}s')
        return result

    return into


def log_methods(format: str):
    """Декоратор для логирования класса."""
    def decorator(my_class):
        for method in dir(my_class):
            if method.startswith('__'):
                continue
            value = getattr(my_class, method)
            if hasattr(value, '__call__'):
                decor = sub_log(my_class, value, format)
                setattr(my_class, method, decor)
        return my_class

    return decorator


@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('тут метод test sum 1.')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("тут метод test sum 1 у наследника.")

    def test_sum_2(self):
        print("тут метод test sum 2 у наследника.")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
