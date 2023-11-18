films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
selected_films = []


for i in range(int(input("Сколько фильмов хотите добавить? "))):
    film_input = input("Введите название фильма: ")
    if film_input in films:
        selected_films.append(film_input)
    else:
        print(f"Ошибка: фильма {film_input} у нас нет :(")

print(f"Ваш список любимых фильмов: {', '.join(selected_films)}")
