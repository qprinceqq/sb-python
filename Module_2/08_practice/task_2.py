def to_find_key(obj, key, depth):
    if depth >= 1:
        if key in obj:
            return obj[key]
    else:
        return None

    for x in obj.values():
        if type(x) is dict:
            result = to_find_key(x, key, depth - 1)
            if result:
                break
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какhой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Введите искомый ключ: ')
choise = input("Хотите ввести максимальную глубину? Y/N: ").lower()
maximum_depth = 100
if choise == 'y':
    maximum_depth = int(input('Введите максимальную глубину: '))
print(f'Значение ключа: {to_find_key(site, key, maximum_depth)}')
