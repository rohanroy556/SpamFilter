from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Monkey can live upto 30 years.')

answer = tkinter.messagebox.askquestion('Question1', 'Do you like silly faces?')
if answer == 'yes':
    print('g===D~')

root.mainloop()
