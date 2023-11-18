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


text = open("text.txt", "r")
read = text.read()
text.close()

letters_dict, total = get_dict_counter(read)
sorted_letters_dict = sorted(letters_dict.items(), key=lambda x: (-x[1], x[0]))

analysis = open("analysis.txt", "w")
for letter, quantity in sorted_letters_dict:
    frequency = round(quantity / total, 3)
    analysis.write(f"{letter} {frequency}\n")

analysis.close()
