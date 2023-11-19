def check_permission_decorator(required_permission: str):
    user_permissions = ['admin']

    def check_permission(func):
        def wrapper(*args, **kwargs):
            if required_permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")

        return wrapper

    return check_permission


@check_permission_decorator('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission_decorator('user')
def add_comment():
    print('Добавляем комментарий')


try:
    delete_site()
    add_comment()
except Exception as e:
    print(e)
