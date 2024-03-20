import tkinter as tk

from constantes import colores
from ui.cubo.ventana import ventana_de_cubo

DIMENSION_POR_DEFECTO = 3


def ventana_inicial():
    ventana = tk.Tk()
    ventana.config(bg=colores.VERDE_1)
    ventana.geometry('200x200')

    def abrir():
        ventana.destroy()
        abrir_ventana()

    button = tk.Button(ventana, text='Open new cube', command=abrir)
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    return ventana


def abrir_ventana():
    ventana = ventana_de_cubo(DIMENSION_POR_DEFECTO)
    ventana.mainloop()
