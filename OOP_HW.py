class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.courses_in_progress = []
        self.courses_complete = []
        self.grades = {}

    def average_grade(self):
        grades_sum = 0
        marks_total = 0
        for number in self.grades.values():
            for grade in number:
                grades_sum += grade
                marks_total += 1
        avr_grade = grades_sum / marks_total
        return round(avr_grade, 2)

    def rate_lector(self, lector, course, grade):
        if grade in range(1, 11):
            if isinstance(lector, Lector) and course in self.courses_in_progress and course in lector.courses_attached:
                if course in lector.grades:
                    lector.grades[course] += [grade]
                else:
                    lector.grades[course] = [grade]
            else:
                return 'Error'
        else:
            return 'Error'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
            f"Средняя оценка за домашние задания: {self.average_grade()}\n"\
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"\
            f"Завершённые курсы: {', '.join(self.courses_complete)}\n"

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Сравнение невозможно"
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return "Сравнение невозможно"
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return "Сравнение невозможно"
        return self.average_grade() == other.average_grade()


class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def average_grade(self):
        grades_sum = 0
        marks_total = 0
        for number in self.grades.values():
            for grade in number:
                grades_sum += grade
                marks_total += 1
        avr_grade = grades_sum / marks_total
        return round(avr_grade, 2)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
            f"Средняя оценка за лекции: {self.average_grade()}\n"

    def __lt__(self, other):
        if not isinstance(other, Lector):
            return "Сравнение невозможно"
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lector):
            return "Сравнение невозможно"
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lector):
            return "Сравнение невозможно"
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def give_mark(self, student, course, grade):
        if grade in range(1, 11):
            if isinstance(student,
                          Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Error'
        else:
            return 'Error'

    def __str__(self):
        return f"Имя: {self.name}\n"\
            f"Фамилия: {self.surname}\n"


first_student = Student('Bobbi', 'Kotik', 26)
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Java']

second_student = Student('Keanu', 'Rewez', 18)
second_student.courses_in_progress += ['Python']
second_student.courses_complete += ['C++']

third_student = Student('Trevor', 'Smith', 41)
third_student.courses_in_progress += ['Java']
third_student.courses_in_progress += ['C++']

good_teacher = Lector('Vic', 'Miller')
good_teacher.courses_attached += ['Python']

bad_teacher = Lector('Mike', 'Brown')
bad_teacher.courses_attached += ['Java']
bad_teacher.courses_attached += ['C++']

good_reviewer = Reviewer('Misha', 'Shkredov')
good_reviewer.courses_attached += ['Python']
good_reviewer.courses_attached += ['Java']

bad_reviewer = Reviewer('Vitalii', 'Kazunov')
bad_reviewer.courses_attached += ['Java']
bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['C++']

good_reviewer.give_mark(first_student, 'Python', 10)
good_reviewer.give_mark(first_student, 'Python', 10)
good_reviewer.give_mark(first_student, 'Python', 9)
good_reviewer.give_mark(first_student, 'Python', 9)
good_reviewer.give_mark(first_student, 'Java', 10)
good_reviewer.give_mark(first_student, 'Java', 10)
good_reviewer.give_mark(first_student, 'Java', 10)
good_reviewer.give_mark(first_student, 'Java', 10)

good_reviewer.give_mark(second_student, 'Python', 7)
good_reviewer.give_mark(second_student, 'Python', 9)
good_reviewer.give_mark(second_student, 'Python', 8)
good_reviewer.give_mark(second_student, 'Python', 7)

bad_reviewer.give_mark(third_student, 'C++', 1)
bad_reviewer.give_mark(third_student, 'C++', 4)
bad_reviewer.give_mark(third_student, 'C++', 5)
bad_reviewer.give_mark(third_student, 'C++', 2)
bad_reviewer.give_mark(third_student, 'Java', 8)
bad_reviewer.give_mark(third_student, 'Java', 6)
bad_reviewer.give_mark(third_student, 'Java', 3)
bad_reviewer.give_mark(third_student, 'C++', 7)


first_student.rate_lector(good_teacher, 'Python', 10)
first_student.rate_lector(good_teacher, 'Python', 10)
first_student.rate_lector(good_teacher, 'Python', 10)
first_student.rate_lector(good_teacher, 'Python', 10)
first_student.rate_lector(bad_teacher, 'Java', 4)
first_student.rate_lector(bad_teacher, 'Java', 3)
first_student.rate_lector(bad_teacher, 'Java', 7)
first_student.rate_lector(bad_teacher, 'Java', 5)

second_student.rate_lector(good_teacher, 'Python', 9)
second_student.rate_lector(good_teacher, 'Python', 8)
second_student.rate_lector(good_teacher, 'Python++', 8)
second_student.rate_lector(good_teacher, 'Python', 9)
second_student.rate_lector(bad_teacher, 'C++', 6)
second_student.rate_lector(bad_teacher, 'C++', 3)
second_student.rate_lector(bad_teacher, 'C++', 4)
second_student.rate_lector(bad_teacher, 'C++', 8)

third_student.rate_lector(bad_teacher, 'Java', 3)
third_student.rate_lector(bad_teacher, 'Java', 4)
third_student.rate_lector(bad_teacher, 'Java', 1)
third_student.rate_lector(bad_teacher, 'Java', 2)
third_student.rate_lector(bad_teacher, 'Java', 5)


first_student.average_grade()
second_student.average_grade()
third_student.average_grade()
good_teacher.average_grade()
bad_teacher.average_grade()

print(first_student)
print(second_student)
print(third_student)
print(bad_teacher)
print(good_teacher)
print(good_reviewer)
print(bad_reviewer)
print('Сравнение средней оценки студентов:')
print(f'Средняя оценка {first_student.name} {first_student.surname}'
      f' {"<" if first_student.average_grade() <  second_student.average_grade() else ">" if first_student.average_grade() > second_student.average_grade() else "="}'
      f' чем у {second_student.name} {second_student.surname}')
print(f'Средняя оценка {first_student.name} {first_student.surname}'
      f' {"<" if first_student.average_grade() < third_student.average_grade() else ">" if first_student.average_grade() > third_student.average_grade() else "="}'
      f' чем у {third_student.name} {third_student.surname}')
print()
print('Сравнение средней оценки лекторов:')
print(f'Средняя оценка {good_teacher.name} {good_teacher.surname}'
      f' {"<" if good_teacher.average_grade() < bad_teacher.average_grade() else ">" if good_teacher.average_grade() > bad_teacher.average_grade() else "="}'
      f' чем у {bad_teacher.name} {bad_teacher.surname}')
print()

student_list = [first_student, second_student, third_student]
course_selection = input('Укажите название курса для подсчёта средней оценки домашних заданий:')


def course_average_grade(students, course):
    course_grades_sum = 0
    course_grade_num = 0
    for student in students:
        if course in student.courses_in_progress or course in student.courses_complete:
            for number in student.grades[course]:
                course_grades_sum += number
                course_grade_num += 1
    avr_grade = course_grades_sum / course_grade_num
    return print(f'Средняя оценка за домашние задания по всем студентам курса {course} {round(avr_grade, 2)}')


course_average_grade(student_list, course_selection)
print()
lector_list = [good_teacher, bad_teacher]
course_selection = input('Укажите название курса для подсчёта средней оценки за лекции: ')


def course_average_grade(lector, course):
    course_grades_sum = 0
    course_grade_num = 0
    for teacher in lector:
        if course in teacher.courses_attached:
            for number in teacher.grades[course]:
                course_grades_sum += number
                course_grade_num += 1
    avr_grade = course_grades_sum / course_grade_num
    return print(f'Средняя оценка  за лекции всех лекторов курса {course} {round(avr_grade, 2)}')


course_average_grade(lector_list, course_selection)