from tkinter import *

from constantes import cubos
from .widgets_de_cubo import *

def crearVentana():
    # configurar ventana
    ventana = Tk()
    ventana.config(bg=VERDE_1)
    ventana.geometry('700x500')

    # crear y posicionar widget
    frameCentral = _crearFrameCentral(ventana)
    frameCentral.place(relx=.5, rely=.5,anchor=CENTER)

    return ventana

def _crearFrameCentral(raiz: Misc):
    cubo = cubos.SUPERFLIP

    def callback_u():
        cubo.movimiento_u()
        colorarCubo(frameCubo, cubo)

    def callback_u_prima():
        cubo.movimiento_u_prima()
        colorarCubo(frameCubo, cubo)
        
    # crear widgets
    frame = Frame(raiz, padx=10, pady=10, bg=VERDE_2)
    frameCubo = crearFrameCubo(frame, cubo)
    button_u = crear_button_u(frame, callback_u)
    button_u_prima = crear_button_u_prima(frame, callback_u_prima)

    # posicionar widgets
    frameCubo.grid(row=0, column=0)
    button_u_prima.grid(row=0, column=1)
    button_u.grid(row=0, column=2)

    return frame