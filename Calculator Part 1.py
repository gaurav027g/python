from tkinter import*
root = Tk()

equation = StringVar()
calculation = Label(root, textvariable=equation)
equation.set("45+50")
calculation.grid(columnspan=4)

root.mainloop()