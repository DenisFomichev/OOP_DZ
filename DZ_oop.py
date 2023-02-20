class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle(self):
        total = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                total += i
                counter += 1
        if counter != 0:
            return round(total / counter, 2)

    def __lt__(self, other):
        if self.middle() > other.middle():
            return f'Лучший студент - {self.name} {self.surname}'
        else:
            return f'Лучший студент - {other.name} {other.surname}'

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за ДЗ: {self.middle()}\n' f'Курсы в процессе изучения: {self.courses_in_progress}\n' f'Завершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def middle(self):
        total = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                total += i
                counter += 1
        if counter != 0:
            return round(total / counter, 2)

    def __lt__(self, other):
        if self.middle() > other.middle():
            return f'Лучший лектор - {self.name} {self.surname}'
        else:
            return f'Лучший лектор - {other.name} {other.surname}'

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {self.middle()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

some_student = Student('Иван', 'Иванов', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Reviewer')
some_reviewer.courses_attached += ['Python', 'Git']

some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Git', 10)
some_reviewer.rate_hw(best_student, 'Git', 9)
some_reviewer.rate_hw(best_student, 'Git', 4)

some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 3)
some_reviewer.rate_hw(some_student, 'Git', 8)
some_reviewer.rate_hw(some_student, 'Git', 4)

some_lecturer = Lecturer('Some', 'Lectur')
some_lecturer.courses_attached += ['Python', 'Git']
other_lecturer = Lecturer('Giga', 'Shmiga')
other_lecturer.courses_attached += ['Python', 'Git']

best_student.rate_hw(some_lecturer, 'Python', 5)
best_student.rate_hw(some_lecturer, 'Python', 2)
best_student.rate_hw(some_lecturer, 'Python', 4)
best_student.rate_hw(other_lecturer, 'Python', 5)
best_student.rate_hw(other_lecturer, 'Python', 5)
best_student.rate_hw(other_lecturer, 'Python', 5)

print('Оценки лектора (оценивает студент): ', some_lecturer.grades)
print()
print('Оценки студента (оценивает проверяющий): ', best_student.grades)
print()
print(some_reviewer)
print()
print(some_lecturer)
print()
print(other_lecturer)
print()
print(best_student)
print()
print(some_student)
print()
print(best_student.__lt__(some_student))
print()
print(some_lecturer.__lt__(other_lecturer))
print()

students_list = [best_student, some_student]
lecturer_list = [some_lecturer, other_lecturer]


def students_grades(students_list, course):
    sum_grades = 0
    quantity_grades = 0
    for student in students_list:
        if course in student.grades.keys():
            sum_grades += sum(student.grades[course])
            quantity_grades += len(student.grades[course])
    if sum_grades == 0:
        return f'Нет оценок!'
    else:
        return round(sum_grades / quantity_grades, 2)


def lecturers_grades(lecturer_list, course):
    sum_grades = 0
    quantity_grades = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades.keys():
            sum_grades += sum(lecturer.grades[course])
            quantity_grades += len(lecturer.grades[course])
    if sum_grades == 0:
        return f'Нет оценок!'
    else:
        return round(sum_grades / quantity_grades, 2)


print(f'Средняя оценка студентов по курсу "Git": {students_grades(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Python": {students_grades(students_list, "Python")}')
print(f'Средняя оценка лекторов по курсу "Python": {lecturers_grades(lecturer_list, "Python")}')