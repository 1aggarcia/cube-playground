from tkinter import *

from modelos.cubo import Cubo
from .de_cubo import crearLabelCubo, crearFrameCubo

CUBO_RESUELTO = Cubo.generar(3)
MI_CUBO = Cubo (
    U=
        [['U1', 'D2'],
        ['U3', 'U3']],
    D=
        [['R1', 'D2'],
        ['D3', 'L4']],
    F=
        [['F1', 'F2'],
        ['B3', 'R4']],
    B=
        [['F1', 'B2'],
        ['D3', 'B4']],
    L=
        [['L1', 'L2'],
        ['L3', 'U4']],
    R=
        [['R1', 'R2'],
        ['B3', 'F4']]
)

def crearVentana():
    # configurar ventana
    ventana = Tk()
    ventana.config(bg='#4fe3a5')
    ventana.geometry('550x350')

    # crear y posicionar widget
    frameCentral = _crearFrameCentral(ventana)
    frameCentral.place(relx=.5, rely=.5,anchor=CENTER)

    return ventana

def _crearFrameCentral(raiz: Misc):
    frame = Frame(raiz, padx=10, pady=10, bg='#189a64')

    cubo = MI_CUBO
    # crear widgets
    frameCubo = crearFrameCubo(frame, cubo)
    labelCubo = crearLabelCubo(frame, cubo)

    # posicionar widgets
    frameCubo.grid(row=0, column=0)
    labelCubo.grid(row=0, column=1)

    return frame