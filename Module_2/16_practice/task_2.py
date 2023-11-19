def callback_d(route):
    callback_d.app = {}
    def callback(func):
        callback_d.app[route] = func
        return func

    return callback


@callback_d('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


# Основной код

route = callback_d.app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
