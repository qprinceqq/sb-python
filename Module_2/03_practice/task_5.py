violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56], ['Halo', 4.9],
                  ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76],
                  ['Blue Dress', 4.29], ['Clean', 5.83]]

sum = 0.00
for i in range(int(input("Сколько песен выбрать? "))):
    song_name = input(f"Название {i+1}-й песни: ")
    for x in violator_songs:
        if x[0] == song_name:
            sum += x[1]
print(f"Общее время звучания песен — {round(sum, 2)} минуты")
