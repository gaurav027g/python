import time
print(time.time())

def numbers(max):
    time1 = time.time()
    for p in range(0,max):
         print(p)
    time2 = time.time()
    print(str(time2 - time1))
print(numbers(100))
print(numbers(400))

print(time.asctime())

birthdate = (2009, 5, 27, 12, 10, 36, 2, 0, 0)
print(time.asctime(birthdate))

print(time.localtime())

t = time.localtime()
year = t[0]
month = t[1]
day = t[2]

print(year)
print(month)
print(day)

print(str(day) + "/" + str(month) + "/" + str(year))

for p in range(0,5):
     print(p)

for p in range(0,5):
     print(p)
     time.sleep(0.7)
