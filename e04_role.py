# You will create three Class: Person, Student, Teacher.


class Person:
    def __init__(self, firstName, lastName):
        self.fristName = firstName
        self.lastName = lastName

    def introduce(self):
        print("Hello I am " + self.fristName + self.lastName + ", I am a Person!")

    def get_info(self):
        return self.fristName, self.lastName

class Student(Person):
    def introduce(self):
        print("Hello I am " + self.fristName + self.lastName+ ", I am a Student!")

class Teacher(Person):
    def introduce(self):
        print("Hello I am " + self.fristName + self.lastName + ", I am a Teacher!")

p = Person("Itachi","Uchiha")
s = Student("Naruto ","Uzumaki ")
t = Teacher("Kakashi","Hatake")
info = p.get_info()
info = s.get_info()
info = t.get_info()
print(type(info))
p.introduce()
s.introduce()
t.introduce()


