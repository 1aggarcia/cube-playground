import tkinter as tk

from constantes import colores
from constantes.enums import Ventana
from ui.cubo.ventana import ventana_de_cubo
from ui.ursina.ventana import ventana_ursina

DIMENSION_POR_DEFECTO = 2


def ventana_inicial():
    ventana = tk.Tk()
    ventana.config(bg=colores.VERDE_1)
    ventana.geometry('300x200')

    def abrir(destino: Ventana):
        ventana.destroy()
        abrir_ventana(destino)

    button_cubo = tk.Button(ventana, text='Open new cube',
                            command=lambda: abrir(Ventana.Cubo))
    button_ursina = tk.Button(ventana, text='Ursina (Beta)',
                            command=lambda: abrir(Ventana.Ursina))

    button_cubo.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
    button_ursina.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

    return ventana


def abrir_ventana(destino: Ventana):
    if destino == Ventana.Ursina:
        app = ventana_ursina(DIMENSION_POR_DEFECTO)
        app.run()
    else:
        ventana = ventana_de_cubo(DIMENSION_POR_DEFECTO)
        ventana.mainloop()
