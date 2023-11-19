from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """Декоратор для декораторов"""
    def into_1(*args, **kwargs) -> Callable:
        def into_2(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)

        return into_2

    return into_1


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    def wrapper(*args_wrap, **kwargs_wrap):
        print(f"Переданные арги и кварги в декоратор: {args}, {kwargs}")
        return func(*args_wrap, **kwargs_wrap)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
