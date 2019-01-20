from tkinter import *

root = Tk()

def printName():
    print("Hello my name is rohan")

def eventButton(event):
    print("Yo Rohan")

button_1 = Button(root, text="Print my name", command=printName)
button_1.pack()
button_2 = Button(root, text="Event button")
button_2.bind("<Button-1>", eventButton)
button_2.pack()

root.mainloop()