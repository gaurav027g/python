class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age

Student1 = Students("Bob", 16)
Student2 = Students("Tom", 18)

print(hasattr(Student1,"name"))

print(hasattr(Student2, "age"))

print(getattr(Student1,"age"))

print(getattr(Student2, "name"))

print(hasattr(Student1, "grade"))

setattr(Student1, 'grade', "10th")

print(hasattr(Student1,"grade"))

delattr(Student1, "grade")

print(hasattr(Student1, "grade"))


    
 