from tkinter import *

from constantes.colores import *
from modelos.cubo import *
from .widgets_de_cubo import *

CUBO_RESUELTO = generarCubo(3)
MI_CUBO = crearCuboDeTexto(
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
    cubo = MI_CUBO

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