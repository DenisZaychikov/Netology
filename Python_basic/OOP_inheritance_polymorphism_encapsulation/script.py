def get_average_person_mark(obj):
    common_mark = 0
    marks_amount = 0
    if not obj.grades:
        return '-'
    for values in obj.grades.values():
        common_mark += sum(values)
        marks_amount += len(values)
    return common_mark / marks_amount


def get_average_students_mark(course, students):
    common_mark = 0
    marks_amount = 0
    if not students:
        return '-'
    for student in students:
        if course in student.grades:
            common_mark += sum(student.grades['course'])
            marks_amount += len(student.grades['course'])
    return f'Средняя оценка студентов по курсу {course} равна {common_mark / marks_amount}'


def get_average_lecturers_mark(course, lecturers):
    common_mark = 0
    marks_amount = 0
    if not lecturers:
        return '-'
    for lecturer in lecturers:
        if course in lecturer.grades:
            common_mark += sum(lecturer.grades['course'])
            marks_amount += len(lecturer.grades['course'])
    return f'Средняя оценка декторов по курсу {course} равна {common_mark / marks_amount}'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_courses_in_progress(self):
        if not self.courses_in_progress:
            return '-'
        elif len(self.courses_in_progress) == 1:
            return ''.join(self.courses_in_progress)
        return ', '.join(self.courses_in_progress)

    def get_finished_courses(self):
        if not self.finished_courses:
            return '-'
        elif len(self.finished_courses) == 1:
            return ''.join(self.finished_courses)
        return ', '.join(self.finished_courses)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {get_average_person_mark(self)}
        Курсы в процессе изучения: {self.get_courses_in_progress()}
        Завершенные курсы: {self.get_finished_courses()}'''

    def __gt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return get_average_person_mark(self) > get_average_person_mark(
                other)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {get_average_person_mark(self)}'''

    def __gt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return get_average_person_mark(self) > get_average_person_mark(
                other)
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        return f'''
        Имя: {self.name}
        Фамилия: {self.surname}'''
