from tkinter import*
root = Tk()

def random():
    print("This is a statement")

mainMenu = Menu(root)
root.configure(menu=mainMenu)
subMenu = Menu(mainMenu)

mainMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New File", command=random)
subMenu.add_command(label="New Window", command=random)
subMenu.add_separator()
subMenu.add_command(label="Open Folder", command=random)
subMenu.add_command(label="Open Recent", command=random)

root.mainloop()