from codecs import strict_errors


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        '''Rate Lecturer'''
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
            ( course in self.courses_in_progress or course in self.courses_in_progress ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
    
    def __str__(self):
        str_result = ''
        str_result += f'Имя: {self.name}\n'
        str_result += f'Фамилия: {self.surname}\n'
        str_result += f'Средняя оценка за домашние задания: {round(self._avg_grade(), 2)}\n'
        str_result += 'Курсы в процессе изучения: '
        i = 0
        for item in self.courses_in_progress:
            str_result += item.__str__()
            if i < len(self.courses_in_progress) - 1:
                str_result += ', '
            else:
                str_result += '\n'
            i += 1
        str_result += ('Завершенные курсы: ')
        i = 0
        for item in self.finished_courses:
            str_result += item.__str__()
            if i < len(self.finished_courses) - 1:
                str_result += ', '
            i += 1
        return str_result

    def _avg_grade(self):
        alist = []
        for gr_list in self.grades.values():
            alist += gr_list
        if len(alist) > 0:
            return sum(alist) / float(len(alist))
        else:
            return 0.0
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        str_result = ''
        str_result += f'Имя: {self.name}\n'
        str_result += f'Фамилия: {self.surname}\n'
        str_result += f'Средняя оценка за лекции: {round(self._avg_grade(), 1)}'
        return str_result

    def __lt__(self, another):
        if isinstance(another, Lecturer):
            return self._avg_grade() < another._avg_grade()

    def _avg_grade(self):
        alist = []
        for gr_list in self.grades.values():
            alist += gr_list
        if len(alist) > 0:
            return sum(alist) / float(len(alist))
        else:
            return 0.0


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
        str_result = ''
        str_result += f'Имя: {self.name}\n'
        str_result += f'Фамилия: {self.surname}'
        return str_result

def avg_hw_grade(students_list, course_name):
    grades_lists = []
    for student in students_list:
        for course, grades in student.grades.items():
            if course == course_name:
                grades_lists += grades

    if len(grades_lists) > 0:
        return sum(grades_lists) / float(len(grades_lists))
    else:
        return 0.0

def avg_lcr_grade(lectirers_list, course_name):
    grades_lists = []
    for lecturer in lectirers_list:
        for course, grades in lecturer.grades.items():
            if course == course_name:
                grades_lists += grades

    if len(grades_lists) > 0:
        return sum(grades_lists) / float(len(grades_lists))
    else:
        return 0.0


# students
first_student = Student('First', 'Student', 'male')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Введение в программирование']
#
second_student = Student('Second', 'Student', 'female')
second_student.courses_in_progress += ['Cpp']
second_student.finished_courses += ['Введение в программирование']

# reviewers
first_reviewer = Reviewer('First', 'Reviewer')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']
#
second_reviewer = Reviewer('Second', 'Reviewer')
second_reviewer.courses_attached += ['Cpp']

# lecturers
first_lecturer = Lecturer('First', 'Lecturer')
first_lecturer.courses_attached += ["Git"]
#
second_lecturer = Lecturer('Second', 'Lecturer')
second_lecturer.courses_attached += ["Git"]
second_lecturer.courses_attached += ["Python"]
second_lecturer.courses_attached += ["Cpp"]

## reviewers rate students
first_reviewer.rate_hw(first_student, 'Python', 6)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Git', 10)
first_reviewer.rate_hw(second_student, 'Python', 10)    # Не пройдёт, потому что second_student не умеет в Python
first_reviewer.rate_hw(second_student, 'Git', 10)       # Не пройдёт, потому что second_student не умеет в Git
#
second_reviewer.rate_hw(first_student, 'Python', 8)       # Не пройдёт, потому что second_reviewer не умеет в Python
second_reviewer.rate_hw(first_student, 'Cpp', 8)        # Не пройдёт, потому что first_student не умеет в Cpp
second_reviewer.rate_hw(second_student, 'Python', 8)      # Не пройдёт, потому что second_reviewer не умеет в Python
second_reviewer.rate_hw(second_student, 'Cpp', 8)

## students rate lecturers
first_student.rate_lc(first_lecturer, 'Python', 8)  # Не пройдёт, потому что first_lecturer не умеет в Python
first_student.rate_lc(first_lecturer, 'Git', 5)
first_student.rate_lc(second_lecturer, 'Git', 7)
first_student.rate_lc(second_lecturer, 'Git', 8)
first_student.rate_lc(second_lecturer, 'Git', 9)
#
second_student.rate_lc(second_lecturer, 'Cpp', 10)
 
print(f'first_student: {first_student.grades}')
print(f'second_student: {second_student.grades}')
print(f'first_lecturer: {first_lecturer.grades}')
print(f'second_lecturer: {second_lecturer.grades}')
print('')
print('Средняя оценка за ДЗ на курсе Git: ', avg_hw_grade([first_student, second_student], 'Git') )
print('Средняя оценка за лектора на курсе Git: ',  avg_lcr_grade([first_lecturer, second_lecturer], 'Git') )
print('')
print(first_student)
print('')
print(second_student)
print('')
print(first_lecturer)
print('')
print(second_lecturer)
print('')
if first_lecturer > second_lecturer:
    print("first_lecturer круче, чем second_lecturer")
elif first_lecturer < second_lecturer:
    print("second_lecturer круче, чем first_lecturer")
else:
    print("first_lecturer и second_lecturer равны")

