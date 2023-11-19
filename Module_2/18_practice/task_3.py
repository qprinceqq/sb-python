import requests
import json


# Обращаемся к API
response = requests.get('https://swapi.dev/api/starships/')
ships_data = response.json()

# Находим информацию о корабле Millennium Falcon
millennium_falcon = next((ship for ship in ships_data['results'] if ship['name'] == 'Millennium Falcon'), None)

# Получаем информацию о пилотах коробля
pilots_info = []
for pilot_url in millennium_falcon['pilots']:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': pilot_data['homeworld'],
        'homeworld_info': requests.get(pilot_data['homeworld']).json()
    }
    pilots_info.append(pilot_info)

# Формируем информацию о корабле Millennium Falcon
millennium_falcon_info = {
    'название': millennium_falcon['name'],
    'максимальная скорость': millennium_falcon['max_atmosphering_speed'],
    'класс': millennium_falcon['starship_class'],
    'список пилотов': pilots_info
}

# Выводим информацию в консоль
print(millennium_falcon_info)

# Записываем информацию в JSON-файл
with open('millennium_falcon_info.json', 'w') as file:
    json.dump(millennium_falcon_info, file, indent=4)