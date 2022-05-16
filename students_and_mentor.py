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
            lecturer.grades[course] = [grade]

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# cool_review 
cool_review = Reviewer('Some', 'Buddy')
cool_review.courses_attached += ['Python']

# simple_lecturer
simple_lecturer = Lecturer('Anoth', 'Erone')
simple_lecturer.courses_attached += ["Cpp"]

# cool_lecturer
cool_lecturer = Lecturer('Thebe', 'Stone')
cool_lecturer.courses_attached += ["Cpp"]
cool_lecturer.courses_attached += ["Python"]

# rate
cool_review.rate_hw(best_student, 'Python', 10)
cool_review.rate_hw(best_student, 'Python', 10)
cool_review.rate_hw(best_student, 'Python', 10)

best_student.rate_lc(simple_lecturer, 'Python', 8)
best_student.rate_lc(simple_lecturer, 'Cpp', 5)

best_student.rate_lc(cool_lecturer, 'Python', 10)
best_student.rate_lc(cool_lecturer, 'Cpp', 10)
 
print(best_student.grades)
print(simple_lecturer.grades)
print(cool_lecturer.grades)