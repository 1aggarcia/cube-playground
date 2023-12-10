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

    def callback():
        cubo.girarMatrizAntihorario(Cara.U)
        cubo.girarMatrizAntihorario(Cara.D)
        colorarCubo(frameCubo, cubo)
        
    # crear widgets
    frame = Frame(raiz, padx=10, pady=10, bg=VERDE_2)
    frameCubo = crearFrameCubo(frame, cubo)
    labelCubo = crearLabelCubo(frame, cubo)
    buttonCubo = crearButtonCubo(frame, callback)

    # posicionar widgets
    frameCubo.grid(row=0, column=0)
    labelCubo.grid(row=0, column=1)
    buttonCubo.grid(row=1)

    return frame