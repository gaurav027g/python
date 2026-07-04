f = open("testfile.txt", "w")
#print(f.read())

print(f.write("how are you feeling today?"))
f.close()
f = open("testfile.txt", "r")
print(f.read())


n = open("testfile.txt", "w")
print(n.write("hey i am bob"))

n = open("testfile.txt", "r")
print(n.read())
