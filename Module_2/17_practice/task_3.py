from collections import Counter


def can_be_poly(s: str) -> bool:
    """Проверка на полиндром"""
    letters_dict = Counter(s.strip())
    not_couple_count = sum(1 for x in letters_dict.values() if x % 2 != 0)
    return not_couple_count <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
