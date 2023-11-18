first_tour = open("first_tour.txt", "r")
second_tour = open("second_tour.txt", "w")
lines = first_tour.readlines()
first_tour.close()

count = 1
to_second_tour = []
min_score = int(lines[0])
for line in lines[1:]:
    surname, name, score = line.split()
    if int(score) > min_score:
        to_second_tour.append(f"{str(count)}) {name[0].upper()}. {surname.title()} {score}")
        count += 1

second_tour.write(str(count - 1) + "\n")
for x in to_second_tour:
    second_tour.write(x + "\n")

second_tour.close()
