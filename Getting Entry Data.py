from tkinter import*
root = Tk()

def evaluate():
    data = e.get()

e = Entry(root)
e.bind("<Return>", evalute)

root.mainloop()