from tkinter import *

from modelos.cubo import Cubo
from .de_cubo import crearLabelCubo, crearFrameCubo

def crearVentana():
    # configurar ventana
    ventana = Tk()
    ventana.config(bg='#4fe3a5')
    ventana.geometry('700x450')

    # crear y posicionar widget
    frameCentral = _crearFrameCentral(ventana)
    frameCentral.place(relx=.5, rely=.5,anchor=CENTER)

    return ventana

def _crearFrameCentral(raiz: Misc):
    frame = Frame(raiz, padx=10, pady=10, bg='#189a64')

    cubo3 = Cubo.generar(3)
    # crear widgets
    frameCubo = crearFrameCubo(frame, cubo3)
    labelCubo = crearLabelCubo(frame, cubo3)

    # posicionar widgets
    frameCubo.grid(row=0, column=0)
    labelCubo.grid(row=0, column=1)

    return frame