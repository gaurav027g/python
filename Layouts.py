from tkinter import*
root = Tk()

topFrame = Frame(root)
topFrame.pack()

botFrame = Frame(root)
botFrame.pack(side=BOTTOM)

Button1 = Button(topFrame,text = "Click Me!", fg = "Blue")
Button1.pack(side=LEFT)

Button2 = Button(topFrame,text = "Hello!", fg = "Red")
Button2.pack()

Button3 = Button(botFrame,text = "Click Me!", fg = "Blue")
Button3.pack(side=LEFT)

Button4 = Button(botFrame,text = "Hello!", fg = "Red")
Button4.pack()

root.mainloop()