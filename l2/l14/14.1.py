class GroupFull(Exception):
    pass
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender=gender
        self.age=age
        self.first_name=first_name
        self.last_name=last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender,age,first_name,last_name)
        self.record_book=record_book

    def __str__(self):
        return f'{super().__str__()}, record book: {self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group)>=10:
            raise GroupFull('Число студентов переполнено')
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(s) for s in  self.group)

        return f'Number:{self.number}\n {all_students} '

gr=Group('PD1')

genders=['Male','Male','Male','Male','Male','Male','Male','Male','Male','Male']
ages=[18,18,19,23,22,23,20,20,19,19]
Name=['Толик','Андрей','Никита','Жора','Михей','Витя','Иван','Руслан','Вова','Дима','Адиль']
LastName=['Толиков','Андреев','Никитин','Чупрун','Каширин','Андрийчук','Попов','Димаскин','Камышин','Русланков','Анатовлен']


for i in range(10):
    student=Student(genders[i],ages[i],Name[i],LastName[i],f'RB{i}')
    gr.add_student(student)

try:
    New_student=Student('Female',22,'Vika','Popova','RB11')
    gr.add_student(New_student)

except GroupFull as e:
    print(f'Ошибка: {e}')

print(gr)
