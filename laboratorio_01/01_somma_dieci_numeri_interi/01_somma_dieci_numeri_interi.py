from cProfile import label
import string
from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Somma dei primi 10 numeri interi")
root.geometry("600x30+200+200")

def somma_dieci_interi():
    message = ""
    total = 0
    for x in range(1, 11):
        total += x
        if x == 10:
            message += str(x)
            break
        message += str(x) + " +"
    
    message += " = " + str(total)

    return message

label = Label(root, text=somma_dieci_interi())

label.pack()

root.mainloop()