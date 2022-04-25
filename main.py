class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rang(self,lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_rating(self):
        a = 0
        for i in self.grades.values():
            a += sum(i) / len(i)
        return  round(a / len(self.grades),1)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_rating()}\n'
                f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {",".join(self.finished_courses)}\n----------------------')

    def __lt__(self,other_student):
        if not isinstance(other_student,Student):
            return print('Не могу сравнить! Не класс Студент')
        return self.average_rating() < other_student.average_rating()
        # if isinstance(other_student, Student):
        #     return self.average_rating() < other_student.average_rating()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    #def __init__(self, name, surname):
        #print('Создан экземпляр класса')
    def average_rating(self):
        a = 0
        for i in self.grades.values():
            a += sum(i) / len(i)
        return  round(a / len(self.grades),1)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_rating()}\n--------------------'

    def __lt__(self,other_lector):
        if not isinstance(other_lector,Lecturer):
            return print('Не могу сравнить! Не класс Лектор')
        return self.average_rating() < other_lector.average_rating()

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
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n--------------------'


best_student = Student('Clarissa', 'Starling', 'female')
best_student.courses_in_progress += ['Python', 'Java', 'C#', 'Linux', 'Git', 'SQL']
best_student.finished_courses += ['Введение в программирование']

second_student = Student('Bill', 'Buffalo', 'male')
second_student.courses_in_progress += ['Python', 'Java', 'C#', 'Linux', 'Git', 'SQL']
second_student.finished_courses += ['Введение в программирование']

first_Reviewer = Reviewer('Jack','Crowford')
first_Reviewer.courses_attached += ['Python','Java','C#']
first_Reviewer.rate_hw(best_student, 'Python', 10)
first_Reviewer.rate_hw(best_student, 'Java', 8)
first_Reviewer.rate_hw(best_student, 'C#', 10)

second_Reviewer = Reviewer('Frederic','Chilton')
second_Reviewer.courses_attached += ['Python','Java','C#']
second_Reviewer.rate_hw(second_student, 'Python', 7)
second_Reviewer.rate_hw(second_student, 'Java', 6)
second_Reviewer.rate_hw(second_student, 'C#', 10)

first_Lecturer = Lecturer('Doctor','Lector')
first_Lecturer.courses_attached += ['Linux','Git','SQL']
second_Lecturer = Lecturer('Katrin','Martin')
second_Lecturer.courses_attached += ['Linux','Git','SQL']

best_student.rang(first_Lecturer, 'Linux', 6)
best_student.rang(first_Lecturer, 'Git', 7)
best_student.rang(first_Lecturer, 'SQL', 9)
best_student.rang(second_Lecturer, 'Linux', 10)
best_student.rang(second_Lecturer, 'Git', 10)
best_student.rang(second_Lecturer, 'SQL', 10)

second_student.rang(first_Lecturer, 'Linux', 1)
second_student.rang(first_Lecturer, 'Git', 2)
second_student.rang(first_Lecturer, 'SQL', 3)
second_student.rang(second_Lecturer, 'Linux', 10)
second_student.rang(second_Lecturer, 'Git', 5)
second_student.rang(second_Lecturer, 'SQL', 4)

student_list = [best_student,second_student]
lectur_list = [first_Lecturer, second_Lecturer]

def average_rating_all_student(student_list, course):
    summa = []
    for student in student_list:
        summa += student.grades[course]
    print('Средняя оценка всех студентов',round(sum(summa)/len(summa),1))

def average_rating_all_Lecturer(lectur_list, course):
    summa = []
    for lectur in lectur_list:
        summa += lectur.grades[course]
    print('Средняя оценка лектора', round(sum(summa)/len(summa),1))




print(first_Reviewer)
print(second_Reviewer)
print(first_Lecturer)
print(second_Lecturer)
print(best_student)
print(second_student)
print('---------------------------------')
print(best_student.average_rating(),second_student.average_rating())
print(best_student.__lt__(second_student))
print(best_student < second_student)
print(best_student > second_student)
print('---------------------------------')
print(best_student < first_Lecturer)
print(best_student > first_Lecturer)
print('---------------------------------')
print(first_Lecturer.average_rating(),second_Lecturer.average_rating())
print(first_Lecturer > second_Lecturer)

average_rating_all_student(student_list, 'Python')
average_rating_all_Lecturer(lectur_list, 'Linux')

















