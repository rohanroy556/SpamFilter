from tkinter import *

def doNothing():
    print("Ok ok I won't...")

root = Tk()

# *** Menu ***

menu = Menu(root)
root.config(menu=menu, )

fileMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Project...", command=doNothing)
fileMenu.add_command(label="New...", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# *** Toolbar ***

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# *** Statusbar ***

status = Label(root, text="Preparing to do nothing... ", bd=1, relief=SUNKEN,
               anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()