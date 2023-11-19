def how_are_you(func):
    def annoying_func():
        input('Как дела? ')
        print('А у меня не очень!')
        func()

    return annoying_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
