class ball:
    def __init__(self,name):
        self.name = name 
    def hello(self):
      print("hello %s" %self.name)
  
bal = ball("Bob")
bal.hello()