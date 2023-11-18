def get_students_info(students):
    lst = []
    for i in students.keys():
        lst += (students[i]['interests'])

    pairs = []
    for i in students.keys():
        pairs.append((i, students[i]['age']))

    string = ''
    for i in students:
        string += students[i]['surname']
    return lst, pairs, len(string)

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

info = get_students_info(students)
print(f"Список пар «ID студента — возраст»: {info[1]}")
print(f"Полный список интересов всех студентов: {info[0]}")
print(f"Общая длина всех фамилий студентов: {info[2]}")
