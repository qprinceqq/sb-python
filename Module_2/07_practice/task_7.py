def new_zip(obj_1, obj_2):
    obj_1, obj_2 = list(enumerate(obj_1)), list(enumerate(obj_2))
    return ((obj_1[i][1], obj_2[i][1]) for i in range(min(len(obj_1), len(obj_2))))


word = "abcd"
tpl = (10, 20, 30, 40)
g = new_zip(word, tpl)

print(g)
print(*g, sep='\n')
