#List of students
students = {"Jonny":19, "Michael":22, "Bob":24}

print(students["Michael"])

students["Michael"] = 23

print(students["Michael"])
print(students["Jonny"])
print(students["Bob"])

del(students["Michael"])

print(students)