import os

folders_count = 0
files_count = 0
size = 0
os_path = os.path.abspath('./')
if os.path.exists(os_path):
    for files in os.listdir(os_path):
        if os.path.isdir(files):
            folders_count += 1
            size += os.path.getsize(os.path.join(os_path, files))
        else:
            files_count += 1
            size += os.path.getsize(os.path.join(os_path, files))
    print(
        f"{folders_count} - кол-во подкаталогов, {files_count} - кол-во файлов, {round(size / 1024, 2)} КБ - размер файлов")
else:
    print("Такого пути не существует")
