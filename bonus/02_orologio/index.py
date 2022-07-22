#Importo la libreria grafica tkinter e il modulo ttk


from tkinter import *
from tkinter import ttk


from time import strftime

# funzioni

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = Tk() # Creo la root

root.title("Orologio")

label = Label(root, font="ds-digital, 80", foreground="cyan", background="black")

label.pack(anchor="center")

time()# Richiamo la funzione time

mainloop()

