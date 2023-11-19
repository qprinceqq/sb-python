from collections import Counter


def count_unique_characters(message: str) -> int:
    """Подсчёт уникальных символов"""
    chars_dict = Counter(message.lower())
    unique_count = sum(list(filter(lambda x: x == 1, chars_dict.values())))
    return unique_count


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
