students1 = {"Mic": 16, "Jack":18, "Bob":17}

print(students1)

students1.clear()

print(students1)

students1 = {"Mic": 16, "Jack":18, "Bob":17}
print(len(students1))
print(students1.keys())
print(students1.values())

students2 = {"Michael": 19, "Jonny":21, "Dev":19}

print(students2)

students1.update(students2)

print(students1)