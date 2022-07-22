from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Somma dei primi 10 numeri interi") #Definisco il titolo della finestra
root.geometry("600x30+200+200") #Definisco le dimensioni della finestra

sum = (10 * 11)/2 #La somma dei primi 10 numeri interi viene calcolata usando il trucco di Gauss che generalizzato è (n/n(+1))/2

message = f"1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = {int(sum)}"  #Uso una stringa interpolata per creare il messaggio

label = Label(root, text=message) #Creo una label per contenere il messaggio

label.pack() # Stampo la label usando il metodo pack()

root.mainloop()