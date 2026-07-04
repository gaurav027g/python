uFn = input("Enter your file name: ")

file1 = open(uFn, "r")
file2 = open("copiedfile.txt", "w")
print(file2.write(file1.read()))

file1.close()
file2.close()
file2 = open("copiedfile.txt", "r")
print(file2.read())