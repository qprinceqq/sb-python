def validate_reg(line):
    fields = line.split()
    if len(fields) != 3:
        raise IndexError('НЕ присутствуют все три поля')

    username = fields[0]
    email = fields[1]
    age = fields[2]

    if not username.isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')

    if '@' not in email or '.' not in email:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и точку')

    try:
        age = int(age)
        if not (age >= 10 and age <= 99):
            raise ValueError
    except ValueError:
        raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')


with open('registrations.txt', 'r', encoding="utf-8") as file:
    registrations_good_log = open('registrations_good.log', 'w', encoding="utf-8")
    registrations_bad_log = open('registrations_bad.log', 'w', encoding="utf-8")

    for line in file.readlines():
        try:
            validate_reg(line)
            registrations_good_log.write(line)
        except (IndexError, NameError, SyntaxError, ValueError) as e:
            registrations_bad_log.write(f'{line.rstrip()}       {e}\n')

    registrations_good_log.close()
    registrations_bad_log.close()
