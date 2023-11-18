file_name = input("Название файла: ")

if file_name.startswith(("@", "№", "$", "%", "^", "&", "*", "(", ")")):
    print("Ошибка: название начинается недопустимым символом.")
elif not(file_name.endswith((".txt", ".docx"))):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("Файл назван верно.")