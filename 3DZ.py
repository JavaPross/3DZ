class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_info(self):
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class Teacher:
    def __init__(self, name, subject, years_of_experience):
        self.name = name
        self.subject = subject
        self.years_of_experience = years_of_experience
    
    def get_info(self):
        return f"Teacher Name: {self.name}, Subject: {self.subject}, Experience: {self.years_of_experience} years"
    
    def teach(self):
        return f"{self.name} is teaching {self.subject}"

class Classroom:
    def __init__(self, room_number, capacity, equipment):
        self.room_number = room_number
        self.capacity = capacity
        self.equipment = equipment
    
    def get_info(self):
        return f"Classroom: {self.room_number}, Capacity: {self.capacity}, Equipment: {self.equipment}"

class SchoolMember(Student, Teacher, Classroom):
    def __init__(self, name, age, grade, subject, years_of_experience, room_number, capacity, equipment):
        Student.__init__(self, name, age, grade)
        Teacher.__init__(self, name, subject, years_of_experience)
        Classroom.__init__(self, room_number, capacity, equipment)
    
    def get_all_info(self):
        return f"{self.get_info()} | {Teacher.get_info(self)} | {Classroom.get_info(self)}"
    
    def is_teacher(self):
        return isinstance(self, Teacher)

member = SchoolMember("John Doe", 30, "10th", "Mathematics", 5, "Room 101", 30, ["Projector", "Board"])
print(member.get_all_info())
print("Is teacher:", member.is_teacher())
#Я переработал код с машинами свой не придумал
