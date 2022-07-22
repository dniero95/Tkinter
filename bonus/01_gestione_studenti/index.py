
from tkinter import *
from tkinter import ttk 


root = Tk()
root.title("Gestione Studenti")

root.minsize(900, 800) # Imposto le dimensioni minime della finestra

file = open('/Users/Faust/Desktop/developer/python/Tkinter/bonus/01_gestione_studenti/studenti.csv', 'r')
students_list = file.readlines()

for student in students_list:
    label = Label(root, text=student).pack()

mainloop()