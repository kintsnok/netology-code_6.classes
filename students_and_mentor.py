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
        str_result += (f'Имя: {self.name}\n')
        str_result += (f'Фамилия: {self.surname}\n')
        str_result += (f'Средняя оценка за домашние задания: {round(self.avg_grade(), 2)}\n')
        str_result += ('Курсы в процессе изучения: ')
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

    def avg_grade(self):
        alist = []
        for gr_list in self.grades.values():
            alist.append( gr_list )
        flat_list = [item for sublist in alist for item in sublist]
        if len(flat_list) > 0:
            return sum(flat_list) / float(len(flat_list))
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
        str_result += (f'Имя: {self.name}\n')
        str_result += (f'Фамилия: {self.surname}\n')
        str_result += (f'Средняя оценка за лекции: {round(self.avg_grade(), 1)}')
        return str_result

    def avg_grade(self):
        alist = []
        for gr_list in self.grades.values():
            alist.append( gr_list )
        flat_list = [item for sublist in alist for item in sublist]
        if len(flat_list) > 0:
            return sum(flat_list) / float(len(flat_list))
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
        str_result += (f'Имя: {self.name}\n')
        str_result += (f'Фамилия: {self.surname}')
        return str_result

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

# cool_review 
cool_review = Reviewer('Some', 'Buddy')
cool_review.courses_attached += ['Python']
cool_review.courses_attached += ['Git']

# simple_lecturer
simple_lecturer = Lecturer('Anoth', 'Erone')
simple_lecturer.courses_attached += ["Git"]

# cool_lecturer
cool_lecturer = Lecturer('Thebe', 'Stone')
cool_lecturer.courses_attached += ["Git"]
cool_lecturer.courses_attached += ["Python"]

# rate
cool_review.rate_hw(best_student, 'Python', 10)
cool_review.rate_hw(best_student, 'Python', 10)
cool_review.rate_hw(best_student, 'Python', 10)
cool_review.rate_hw(best_student, 'Git', 8)

best_student.rate_lc(simple_lecturer, 'Python', 8)  # Не пройдёт, потому что simple_lecturer не умеет в Python
best_student.rate_lc(simple_lecturer, 'Git', 5)

best_student.rate_lc(cool_lecturer, 'Python', 10)
best_student.rate_lc(cool_lecturer, 'Git', 10)
 
print(best_student.grades)
print(simple_lecturer.grades)
print(cool_lecturer.grades)
print('')
print(best_student)
print('')
print(simple_lecturer)
print('')
print(cool_lecturer)