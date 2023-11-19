import os


def py_path_n_lines_generator(directory='C:/'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as py:
                    read_lines = py.readlines()
                    count = sum([1 for line in read_lines if line.strip() and not line.strip().startswith('#')])
                    yield file_path, count


for file_path, lines_count in py_path_n_lines_generator('./'):
    print(f'{file_path}: {lines_count} строк кода')
