with open("people.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


def check_n_count_list(lines):
    error_log = []
    i = 0
    count = 0
    for x in lines:
        x = x.strip()
        i += 1
        try:
            if len(x) >= 3:
                count += len(x)
            else:
                count += len(x)
                error_log.append(i)
                raise ValueError
        except ValueError:
            pass
    return error_log, count


error_log, count, = check_n_count_list(lines)
for i in error_log: print(f"Ошибка: менее трёх символов в строке {i}.")
print(f"Общее количество символов: {count}")
