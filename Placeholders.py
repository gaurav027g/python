#Sentences
sen1 = "Hey %s, make sure to reach the meeting on time tomorrow"
sen2 = "Hello %s %s, You have been selected by the company"  
sen3 = "I am %s and my age is %d"

#Names
emp1,emp2,emp3 = "Mukesh", "Jonny", "Michael"


print(sen1%(emp1))
print(sen1%(emp2))
print(sen1%(emp3))
print(sen2%("Prashans","Kumar"))
print(sen3%("Gaurav", 18))

