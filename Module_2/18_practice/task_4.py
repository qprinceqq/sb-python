import re


def check_phone_numbers(number):
        if re.match(r'^[89]\d{9}$', number):
            return f"{number}: всё в порядке"
        else:
            return f"{number}: не подходит"


numbers = ['9999999999', '999999-999', '99999x9999']
for number in numbers:
    print(check_phone_numbers(number))
