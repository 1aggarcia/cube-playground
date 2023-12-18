import tkinter as tk

from modelos.cubo import generar_cubo
from modelos.movimiento import Movimiento
from constantes import cubos
from constantes import colores
from constantes.enums import Cara
from . import widgets_de_cubo as widgets

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
    cubo = cubos.SUPERFLIP

    def callback(cara: Cara, direccion: int):
        cubo.mover(Movimiento(cara, direccion, 1, False))
        widgets.colorar_cubo(frame_cubo, cubo)

    # crear widgets
    frame = tk.Frame(raiz, padx=10, pady=10, bg=colores.VERDE_2)
    frame_cubo = widgets.crear_frame_cubo(frame, cubo)
    button_u_prima = widgets.crear_button(frame, Cara.U, -1, callback)
    button_d_prima = widgets.crear_button(frame, Cara.D, -1, callback)
    button_r_prima = widgets.crear_button(frame, Cara.R, -1, callback)
    button_l_prima = widgets.crear_button(frame, Cara.L, -1, callback)
    button_f_prima = widgets.crear_button(frame, Cara.F, -1, callback)
    button_b_prima = widgets.crear_button(frame, Cara.B, -1, callback)

    button_u = widgets.crear_button(frame, Cara.U, 1, callback)
    button_d = widgets.crear_button(frame, Cara.D, 1, callback)
    button_r = widgets.crear_button(frame, Cara.R, 1, callback)
    button_l = widgets.crear_button(frame, Cara.L, 1, callback)
    button_f = widgets.crear_button(frame, Cara.F, 1, callback)
    button_b = widgets.crear_button(frame, Cara.B, 1, callback)

    # posicionar widgets
    frame_cubo.grid(row=0, column=0)

    button_u.grid(row=1, column=1)
    button_d.grid(row=1, column=2)
    button_r.grid(row=1, column=3)
    button_l.grid(row=1, column=4)
    button_f.grid(row=1, column=5)
    button_b.grid(row=1, column=6)

    button_u_prima.grid(row=2, column=1)
    button_d_prima.grid(row=2, column=2)
    button_r_prima.grid(row=2, column=3)
    button_l_prima.grid(row=2, column=4)
    button_f_prima.grid(row=2, column=5)
    button_b_prima.grid(row=2, column=6)

    return frame
