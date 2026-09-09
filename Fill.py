from tkinter import*
root = Tk()

Button1 = Button(None,text = "Click Me!", fg = "Blue")
Button1.pack()

Button2 = Button(None,text = "Hello!", fg = "Red")
Button2.pack(fill=X)

Button3 = Button(None,text = "Click Me!", fg = "Purple")
Button3.pack(side=LEFT, fill=Y)

Button4 = Button(None,text = "Hello!", fg = "Yellow")
Button4.pack()

root.mainloop()