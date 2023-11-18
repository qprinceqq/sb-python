class Student:

    def __init__(self, fullname, group_number, estimation):
        self.fullname = fullname
        self.group_number = group_number
        self.estimation = estimation

    def get_info(self):
        return str("Имя и фамилия студента: {0}, Номер группы: {1}, Оценки студента: {2}".format(self.fullname,
                                                                                                 self.group_number,
                                                                                                 self.estimation))

    def get_average(self):
        estimate_count = 0
        score = 0
        for estimation in self.estimation:
            score += estimation
            estimate_count += 1

        return score / estimate_count


students = []
example = ["ФИ", "Номер группы", "Успеваемость (через пробел)"]
for i in range(int(input("Введите кол-во студентов: "))):
    field = []
    for i in range(3):
        if i == 2:
            field.append(tuple(map(int, input(f"{example[i]}: ").split())))
        else:
            field.append(input(f"{example[i]}: "))
    students.append(Student(field[0], field[1], field[2]))

for i in range(len(students) - 1):
    for j in range(i + 1, len(students)):
        if students[i].get_average() < students[j].get_average():
            temp = students[i]
            students[i] = students[j]
            students[j] = temp

print("\nПосле сортировки: ")
for i in students:
    print(i.get_info())
    print(("Средний балл: {0}".format(i.get_average())))
