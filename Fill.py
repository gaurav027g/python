from tkinter import*
root = Tk()

Button1 = Button(None,text = "Click Me!", fg = "Blue")
Button1.pack(side=LEFT)

Button2 = Button(None,text = "Hello!", fg = "Red")
Button2.pack()

Button3 = Button(None,text = "Click Me!", fg = "Blue")
Button3.pack(side=LEFT)

Button4 = Button(None,text = "Hello!", fg = "Red")
Button4.pack()

root.mainloop()