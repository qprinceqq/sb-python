from random import randint


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    if randint(1, 10) == 1:
        raise [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError][randint(0, 4)]
    return randint(1, 7)


with open("karma.log", "w") as file:
    karma_total = 0
    while karma_total < 500:
        try:
            karma_total += one_day()
        except Exception as e:
            file.write(f"Exception: {e.__class__.__name__}\n")
