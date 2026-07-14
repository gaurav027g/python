class ball:
    def move(self):
        print("I am moving")
    def jump(self):
        self.move()
        print("I am jumping")

instance = ball()
instance.move()
instance.jump()
