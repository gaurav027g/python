f = open("testfile.txt", "a")
f.write("I am the man of my words ")

f.close()

f = open("testfile.txt", "r")
print(f.read())


f = open("testfile.txt", "a+")
f.write(" my name is Avi")

f.close()

f = open("testfile.txt", "r")
print(f.read())