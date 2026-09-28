from tkinter import*
root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()
canvas.create_rectangle(20,20,100,270)
canvas.create_line(0,0,300,250)
canvas.create_polygon(60,50,30,250,250,250,220,50)
root.mainloop()