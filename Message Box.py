from tkinter import*
import tkinter.messagebox
root = Tk()

tkinter.messagebox.showinfo("Window Title", "hey, you know i am a genius")

answer = tkinter.messagebox.askquestion("Question 1", "Are you 18 year old")

if answer == "yes":
    tkinter.messagebox.showinfo("Window Title", "You are an adult")

if answer == "no":
    tkinter.messagebox.showinfo("Window Title", "You are a teenager")

root.mainloop()