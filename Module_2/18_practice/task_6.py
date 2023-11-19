import json

# Открываем и загружаем json файлы
with open('json_old.json', encoding="utf-8") as file_1:
    dict_old = json.load(file_1)

with open('json_new.json', encoding="utf-8") as file_2:
    dict_new = json.load(file_2)

diff_list = ["services", "staff", "datetime"]

# Сравниваем детали, указанные в diff_list, и выводим различия
result = ''
for key in diff_list:
    if dict_old['data'][key] != dict_new['data'][key]:
        result += f', "{str(key)}": ' + str(dict_new['data'][key])
result = '{' + result[2:] + '}'
print(result)

# Выводим различия в отдельный файл result.json
with open('result.json', 'w', encoding="utf-8") as file:
    json.dump(result, file)
