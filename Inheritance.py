class Parent:
    counter = 20
    def __init__(self):
        print("i am a parent")
    def parentFunc(self):
        print("i am a father")
    def setCounter(self,num):
        Parent.counter = num
    def showCounter(self):
        print(Parent.counter)

class Child(Parent):
    def __init__(self):
        print("I am a student")
    def childFunc(self):
        print("i am a son")

c = Child()
c.childFunc()

c = Parent()
c.parentFunc()
print(c.counter)
c.setCounter(30)
c.showCounter()