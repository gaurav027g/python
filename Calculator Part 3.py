from tkinter import*
root = Tk()

equa = ""

equation = StringVar()

calculation = Label(root, textvariable=equation)

equation.set("45+50")

calculation.grid(columnspan=4)

def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

Button0 = Button(root, text="0", command=lambda:btnPress(0))
Button0.grid(row=4,column=3)

Button1 = Button(root, text="1", command=lambda:btnPress(1))
Button1.grid(row=1,column=0)

Button2 = Button(root, text="2", command=lambda:btnPress(2))
Button2.grid(row=1,column=1)

Button3 = Button(root, text="3", command=lambda:btnPress(3))
Button3.grid(row=1,column=2)

Button4 = Button(root, text="4", command=lambda:btnPress(4))
Button4.grid(row=1,column=2)

Button5 = Button(root, text="5", command=lambda:btnPress(0))
Button5.grid(row=1,column=0)

Button6 = Button(root, text="6", command=lambda:btnPress(0))
Button6.grid(row=1,column=0)

Button7 = Button(root, text="7", command=lambda:btnPress(0))
Button7.grid(row=1,column=0)

Button8 = Button(root, text="8", command=lambda:btnPress(0))
Button8.grid(row=1,column=0)

Button9 = Button(root, text="9", command=lambda:btnPress(0))
Button9.grid(row=1,column=0)

Plus = Button(root, text="+", command=lambda:btnPress(0))
Plus.grid(row=1,column=0)

Minus = Button(root, text="-", command=lambda:btnPress(0))
Minus.grid(row=1,column=0)

Multiply = Button(root, text="*", command=lambda:btnPress(0))
Multiply.grid(row=1,column=0)

Divide = Button(root, text="/", command=lambda:btnPress(0))
Divide.grid(row=1,column=0)

root.mainloop()