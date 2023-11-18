def merge_sorted_lists(list1, list2):
    list1 += list2
    list1.sort()
    merge_sorted_list = []
    return [x for x in list1 if x not in merge_sorted_list]


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
print(f"Вывод: {merge_sorted_lists(list1, list2)}")
