from tkinter import*
import random
root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

canvas.create_arc(10,5,150,80, extent=60, style=ARC)
canvas.create_arc(10,30,150,160, extent=60, style=ARC)

canvas.create_text(150,150, text="This is my first GUI text", font=("Times", 15))

root.mainloop()