from tkinter import *

from modelos.cubo import Cubo
from constantes.colores import COLORES_DE_CUBO

def crearLabelCubo(raiz: Misc, cubo: Cubo):
    return Label(raiz, text = str(cubo), bg='#189a64', fg='#ffffff')

def crearFrameCubo(raiz: Misc, cubo: Cubo):
    frame = Frame(raiz, bg='#189a64')

    # crear widgets
    frameL = Frame(frame, width=100, height=100, bg=COLORES_DE_CUBO['L'])
    frameU = Frame(frame, width=100, height=100, bg=COLORES_DE_CUBO['U'])
    frameF = Frame(frame, width=100, height=100, bg=COLORES_DE_CUBO['F'])
    frameD = Frame(frame, width=100, height=100, bg=COLORES_DE_CUBO['D'])
    frameR = Frame(frame, width=100, height=100, bg=COLORES_DE_CUBO['R'])
    frameB = Frame(frame, width=100, height=100, bg=COLORES_DE_CUBO['B'])

    #posicionar widgets
    frameU.grid(row=0, column=1)
    frameL.grid(row=1, column=0)
    frameF.grid(row=1, column=1)
    frameR.grid(row=1, column=2)
    frameB.grid(row=1, column=3)
    frameD.grid(row=2, column=1)

    return frame