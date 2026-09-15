from tkinter import*
root = Tk()

def evaluate():

e = Entry(root)
e.bind("<Return>", evaluate)

root.mainloop()