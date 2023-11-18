def get_dict_counter(text):
    letters = {}
    total = 0
    for char in text:
        if char.isalpha():
            total += 1
            char = char.lower()
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters, total


with open('voina-i-mir.txt', 'r', encoding='windows-1251') as file:
    text = file.read()

letters_dict, total = get_dict_counter(text)
sorted_letters_dict = sorted(letters_dict.items(), key=lambda x: x[1], reverse=True)

with open('letter_statistics.txt', 'w', encoding='utf-8') as file:
    for letter, count in sorted_letters_dict:
        frequency = count / total
        file.write(f"{letter}: {round(frequency, 4)}\n")
