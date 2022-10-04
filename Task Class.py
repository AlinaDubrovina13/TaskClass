class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_1(self):
        coast = 0
        summa_hw = 0
        for v in self.grades.values():
            for i in v:
                coast += 1
                summa_hw += i
        avg_hw = summa_hw / coast
        return round(avg_hw, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.grade_1() < other.grade_1()

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.grade_1()} \nКурсы в процессе обучения: {",".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def grade_2(self):
        coast = 0
        sum_lc = 0
        for v in self.grades.values():
            for i in v:
                coast += 1
                sum_lc += i
        avg_lc = sum_lc / coast
        return round(avg_lc, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.grade_2() < other.grade_2()

    def __str__(self):
        result = (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grade_2()}')
        return result

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = (f'Имя: {self.name} \nФамилия: {self.surname}')
        return result


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['GIT']
student = Student('Ivan', 'Ivanov', 'Male')
student.courses_in_progress += ['Python']
student.finished_courses += ['GIT']
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'GIT']
reviewer = Reviewer('Petr', 'Petrov')
reviewer.courses_attached += ['Python', 'GIT']
lecturer = Lecturer('Alexsey', 'Alekseev')
lecturer.courses_attached += ['Python']
lecturer.courses_attached += ['GIT']
student.rate_lc(lecturer, 'Python', 10)
student.rate_lc(lecturer, 'Python', 10)
student.rate_lc(lecturer, 'GIT', 9)
cool_lecturer = Lecturer('Andrey', 'Andreev')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']
best_student.rate_lc(cool_lecturer, 'Python', 8)
best_student.rate_lc(cool_lecturer, 'Python', 6)
best_student.rate_lc(cool_lecturer, 'GIT', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'GIT', 9)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'GIT', 7)

print(best_student)
print(student)

print(cool_reviewer)
print(reviewer)

print(lecturer)
print(cool_lecturer)

print(best_student < student)
print(lecturer < cool_lecturer)


students_list = [
    {'Python': ['Liza Petrova', 'Maria Kozlova', 'Natasha Rostova']},
    {'GIT': ['Lev Tolstoy', 'Maksim Gorkiy']}
]
lecturers_list = ['Ivan Ivanov', 'Aleksey Alekseev', 'Anton Antonov']

def students_courses_grades(students_list):
    grades_course = {}
    students_courses_grades = 0
    for course in students_list:
        for course_name, student in course.items():
            for name in student:
                i = input(f"Введите оценку за курс {course_name} {name}: ")
                if course_name in grades_course.keys():
                    grades_course[course_name].append(i)
                else:
                    grades_course[course_name] = [i]

    for k, v in grades_course.items():
        for i, el in enumerate(v):
            v[i] = int(el)

    for course, grades in grades_course.items():
        students_courses_grades = {k: sum((v)) / len(v) for k, v in grades_course.items()}

    for k, v in students_courses_grades.items():
            print(f"Средняя оценка по курсу {k}: {round(v, 1)}")

def lecturer_courses_grades(lecturers_list):
    grades_course = {}
    for lecturer in lecturers_list:
        course_name = input(f"Введите курс, который читает {lecturer}: ")
        grade = input(f"Введите оценку за лекции по {course_name} лектора {lecturer}: ")
        if course_name in grades_course.keys():
            grades_course[course_name].append(grade)
        else:
            grades_course[course_name] = [grade]

    for k, v in grades_course.items():
            for i, el in enumerate(v):
                v[i] = int(el)

    for course, grades in grades_course.items():
        lecturer_courses_grades = {k: sum((v)) / len(v) for k, v in grades_course.items()}

    for k, v in lecturer_courses_grades.items():
            print(f"Средняя оценка по курсу {k}: {round(v, 1)}")

lecturer_courses_grades(lecturers_list)
students_courses_grades(students_list)