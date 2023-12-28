import tkinter as tk

from modelos.movimiento import Movimiento
from constantes import cubos
from constantes import colores
from . import dibujar_cubo as dibujar
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

    def realizar_alg(algorithmo: list[str]):
        cubo.ejecutar_algoritmo(algorithmo)
        dibujar.colorar_cubo(frame_cubo, cubo)

    # crear widgets
    frame = tk.Frame(raiz, padx=10, pady=10, bg=colores.VERDE_2)
    frame_cubo = dibujar.crear_frame_cubo(frame, cubo)
    frame_control = control.crear_frame_control(frame, realizar_alg)

    # posicionar widgets
    frame_cubo.grid(row=0, column=0)
    frame_control.grid(row=0, column=1)

    return frame
