word = "abcdefg"
answers = [word[:], word[::-1], word[::2], word[1::2], word[:1], word[:-2:-1], word[3:4], word[len(word) - 3:],
           word[3:5], word[4:2:-1]]
for i in range(10):
    print(f"{i + 1}: {answers[i]}")
