import tkinter as tk
from typing import Literal

from modelos.movimiento import Movimiento
from constantes import cubos
from constantes import colores
from constantes.enums import Cara
from . import widgets_de_cubo as widgets
from . import controlar_cubo as control

OLL = ["R", "U", "R'", "U'", "R'", "F", "R2", "U", "R'", "U'", "F'"]

def crear_ventana():
    # configurar ventana
    ventana = tk.Tk()
    ventana.config(bg=colores.VERDE_1)
    ventana.geometry('700x550')

    # crear y posicionar widget
    frame_central = _crear_frame_central(ventana)
    frame_central.place(relx=.5, rely=.5,anchor=tk.CENTER)

    return ventana


def _crear_frame_central(raiz: tk.Misc):
    cubo = cubos.CUBO_RESUELTO_3
    movimientos = []

    def callback(cara: Cara, direccion: Literal[-1, 1, 2]):
        mov = Movimiento(cara, direccion, 1, False)

        cubo.mover(mov)
        widgets.colorar_cubo(frame_cubo, cubo)
        movimientos.append(mov)
        print(movimientos)

    def callback_algorithmo():
        cubo.ejecutar_algoritmo(OLL)
        widgets.colorar_cubo(frame_cubo, cubo)
        movimientos.extend(OLL)
        print(movimientos)

    # crear widgets
    frame = tk.Frame(raiz, padx=10, pady=10, bg=colores.VERDE_2)
    frame_cubo = widgets.crear_frame_cubo(frame, cubo)
    frame_control = control.crear_frame_control(frame)

    # posicionar widgets
    frame_cubo.grid(row=0, column=0)
    frame_control.grid(row=0, column=1)

    return frame
