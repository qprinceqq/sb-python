import os


def files_path_generator(direct='C:/'):
    for path, _, files_list in os.walk(direct):
        for file in files_list:
            yield os.path.join(path, file)


# Пример использования
for file_path in files_path_generator('./'):
    print(file_path)
