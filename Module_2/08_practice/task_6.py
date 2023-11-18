def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    q = numbers[-1]
    left_nums = [n for n in numbers if n < q]
    midle_nums = [q] * numbers.count(q)
    right_nums = [n for n in numbers if n > q]
    return quick_sort(left_nums) + midle_nums + quick_sort(right_nums)


x = [1, 2, 3, 5, 2, 3, -7, 3, 0, 0, 11, 6]
print(quick_sort(x))
