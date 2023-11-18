violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}

songs_time = 0
for i in range(int(input("Сколько песен выбрать? "))):
    try:
        songs_time += violator_songs[input("Название песни: ")]
    except:
        print("Такой песни нет")

print(f"Общее время звучания песен: {round(songs_time, 2)} минут")
