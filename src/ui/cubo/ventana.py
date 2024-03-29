import tkinter as tk

from constantes import colores
from modelos.cubo import generar_cubo
from ui.cubo.dibujar_cubo import crear_frame_cubo
from ui.cubo.controlar_cubo import crear_frame_control

def ventana_de_cubo(dimension: int):
    # configurar ventana
    ventana = tk.Tk()
    ventana.config(bg=colores.VERDE_1)
    ventana.geometry('1100x600')

    # crear y posicionar widget
    frame_central = _crear_frame_central(ventana, dimension)
    frame_central.place(relx=.5, rely=.5,anchor=tk.CENTER)

    return ventana


def _crear_frame_central(raiz: tk.Misc, dimension: int):
    cubo = generar_cubo(dimension)

    # crear widgets
    frame = tk.Frame(raiz, padx=10, pady=10, bg=colores.VERDE_2)
    frame_cubo = crear_frame_cubo(frame, cubo)
    frame_control = crear_frame_control(frame, cubo)

    # posicionar widgets
    frame_cubo.grid(row=0, column=0)
    frame_control.grid(row=0, column=1)

    return frame
