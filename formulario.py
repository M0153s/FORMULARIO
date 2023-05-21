import csv
from tkinter import Tk , Label, Entry, Button,Text


def guardar_registro():
    nombre= nombre_entry.get()
    edad= edad_entry.get()



    with open('registros.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, edad])

        mostrar_registros()



def mostrar_registros():
    registros_text.delete(1.0, "end")

     
    with open('registros.csv', 'r') as file:
        reader = csv.reader(file)


        for row in reader:
            registros_text.insert("end", f"Nombre: {row[0]}, Edad: {row[1]}\n")


window = Tk()
window.title("Programa de Registro")
window.geometry("400x300")


nombre_label = Label(window, text="Nombre:")
nombre_label.pack()
nombre_entry = Entry(window)
nombre_entry.pack()

edad_label = Label(window, text="Edad:")
edad_label.pack()
edad_entry = Entry(window)
edad_entry.pack()

guardar_button = Button(window, text="Guardar", command=guardar_registro)
guardar_button.pack()

registros_text = Text(window)
registros_text.pack()

mostrar_registros()
window.mainloop()