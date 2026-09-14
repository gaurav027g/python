from tkinter import*
root = Tk()

def leftClick(event):
    print("Left")

def rightClick(event):
    print("Right")

button1 = Button(root, text="Click Me")
button1.bind("<Button-1>", printName)
button1.pack()

root.mainloop()