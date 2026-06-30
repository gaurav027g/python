class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age

Student1 = Students("Bob", 16)
print(Student1.name)
print(Student1.age) 

class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def displayStudent(self):
        return("Student name is " + self.name + " and age is " + str(self.age))
    
Student2 = Students("Bob", 16)
print(Student2.displayStudent())