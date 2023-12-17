import tkinter as tk

from constantes import cubos
from constantes import colores
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
    cubo = cubos.CUBO_RESUELTO

    def callback_u(horario: bool):
        cubo.movimiento_u(horario)
        widgets.colorar_cubo(frame_cubo, cubo)

    def callback_d(horario: bool):
        cubo.movimiento_d(horario)
        widgets.colorar_cubo(frame_cubo, cubo)

    def callback_r(horario: bool):
        cubo.movimiento_r(horario)
        widgets.colorar_cubo(frame_cubo, cubo)

    def callback_l(horario: bool):
        cubo.movimiento_l(horario)
        widgets.colorar_cubo(frame_cubo, cubo)

    # crear widgets
    frame = tk.Frame(raiz, padx=10, pady=10, bg=colores.VERDE_2)
    frame_cubo = widgets.crear_frame_cubo(frame, cubo)
    button_u_prima = widgets.crear_button_u(frame, callback_u, False)
    button_d_prima = widgets.crear_button_d(frame, callback_d, False)
    button_r_prima = widgets.crear_button_r(frame, callback_r, False)
    button_l_prima = widgets.crear_button_l(frame, callback_l, False)

    button_u = widgets.crear_button_u(frame, callback_u, True)
    button_d = widgets.crear_button_d(frame, callback_d, True)
    button_r = widgets.crear_button_r(frame, callback_r, True)
    button_l = widgets.crear_button_l(frame, callback_l, True)

    # posicionar widgets
    frame_cubo.grid(row=0, column=0)

    button_u_prima.grid(row=1, column=1)
    button_d_prima.grid(row=2, column=1)
    button_r_prima.grid(row=3, column=1)
    button_l_prima.grid(row=4, column=1)

    button_u.grid(row=1, column=2)
    button_d.grid(row=2, column=2)
    button_r.grid(row=3, column=2)
    button_l.grid(row=4, column=2)

    return frame
