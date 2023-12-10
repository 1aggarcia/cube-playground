from tkinter import *

from constantes.colores import *
from constantes.cubos import MI_CUBO, CUBO_RESUELTO, SUPERFLIP
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
    frame = Frame(raiz, padx=10, pady=10, bg=VERDE_2)

    global frameCubo
    global cubo
    cubo = SUPERFLIP

    def callback():
        ninos = frameCubo.winfo_children()
        if len(ninos) != 6: # cantidad de cars = 6
            raise ValueError('REQUISITO ROTO')
        cubo.girarMatrizAntihorario(Cara.U)
        for i in range(6):
            dibujarCara(ninos[i], cubo, list(Cara)[i])
        
    # crear widgets
    frameCubo = crearFrameCubo(frame, cubo)
    labelCubo = crearLabelCubo(frame, cubo)
    buttonCubo = crearButtonCubo(frame, callback)

    # posicionar widgets
    frameCubo.grid(row=0, column=0)
    labelCubo.grid(row=0, column=1)
    buttonCubo.grid(row=1)

    return frame