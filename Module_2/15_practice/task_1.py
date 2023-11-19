class File:
    def __init__(self, file_path, mode_open='r'):
        self.file_path = file_path
        self.mode_open = mode_open
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_path, self.mode_open)
        except FileNotFoundError:
            # Если файл не существует, создаем его в режиме записи
            self.file = open(self.file_path, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # Закрываем файл (при условии, что он есть)
        if self.file:
            self.file.close()
        return True


with File('example.txt', 'w') as file:
    file.write('Hello, World!')
