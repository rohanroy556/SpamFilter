from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=250)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 125)
redLine = canvas.create_line(0, 250, 200, 125, fill='red')
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill='green')

canvas.delete(redLine)
canvas.delete(ALL)

root.mainloop()
