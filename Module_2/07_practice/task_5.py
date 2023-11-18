def tpl_sort(tpl):
    numbers = [x for x in tpl if x % 1 == 0]
    if numbers == [x for x in tpl]:
        numbers.sort()
        return numbers

    return tpl


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))
