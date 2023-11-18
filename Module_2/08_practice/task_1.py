def print_in_range(num):
    if num > 0:
        print_in_range(num - 1)
        print(num)


print_in_range(int(input("Введите num: ")))
