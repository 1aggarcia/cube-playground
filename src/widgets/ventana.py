import tkinter as tk

from constantes import cubos
from constantes import colores
from . import widgets_de_cubo as widgets

def crear_ventana():
    # configurar ventana
    ventana = tk.Tk()
    ventana.config(bg=colores.VERDE_1)
    ventana.geometry('700x500')

    # crear y posicionar widget
    frame_central = _crear_frame_central(ventana)
    frame_central.place(relx=.5, rely=.5,anchor=tk.CENTER)

    return ventana

def _crear_frame_central(raiz: tk.Misc):
    cubo = cubos.SUPERFLIP

    def callback_u():
        cubo.movimiento_u()
        widgets.colorar_cubo(frame_cubo, cubo)

    def callback_u_prima():
        cubo.movimiento_u_prima()
        widgets.colorar_cubo(frame_cubo, cubo)

    # crear widgets
    frame = tk.Frame(raiz, padx=10, pady=10, bg=colores.VERDE_2)
    frame_cubo = widgets.crear_frame_cubo(frame, cubo)
    button_u = widgets.crear_button_u(frame, callback_u)
    button_u_prima = widgets.crear_button_u_prima(frame, callback_u_prima)

    # posicionar widgets
    frame_cubo.grid(row=0, column=0)
    button_u_prima.grid(row=0, column=1)
    button_u.grid(row=0, column=2)

    return frame
