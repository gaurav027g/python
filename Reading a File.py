file1 = open("testfile.txt","r")
print(file1.read())

print(file1.read())

print(file1.tell())

print(file1.seek(0,0))

print(file1.read())

print(file1.seek(0,0))

print(file1.read(22))
print(file1.read(22))
print(file1.read(22))
