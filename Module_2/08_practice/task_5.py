def out_list(array):
    if not array:
        return []
    return out_list(array[:-1]) + ([array[-1]] if type(array[-1]) != list else out_list(array[-1]))


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(out_list(nice_list))
