from tkinter import *

from modelos.cubo import Cubo
from constantes.colores import COLORES_DE_CUBO, Cara

TAMANO_DE_CARA = 100 # width y height de una cara

def crearLabelCubo(raiz: Misc, cubo: Cubo):
    return Label(raiz, text = str(cubo), bg='#189a64', fg='#ffffff')

def crearFrameCubo(raiz: Misc, cubo: Cubo):
    frame = Frame(raiz, bg='#189a64')

    # crear widgets
    caraU = dibujarCara(frame, cubo, Cara.U)
    caraL = dibujarCara(frame, cubo, Cara.L)
    caraF = dibujarCara(frame, cubo, Cara.F)
    caraR = dibujarCara(frame, cubo, Cara.R)
    caraB = dibujarCara(frame, cubo, Cara.B)
    caraD = dibujarCara(frame, cubo, Cara.D)

    #posicionar widgets
    caraU.grid(row=0, column=1)
    caraL.grid(row=1, column=0)
    caraF.grid(row=1, column=1)
    caraR.grid(row=1, column=2)
    caraB.grid(row=1, column=3)
    caraD.grid(row=2, column=1)

    return frame

def dibujarCara(raiz: Misc, cubo: Cubo, cara: Cara):
    frame = Frame(raiz, width=TAMANO_DE_CARA, height=TAMANO_DE_CARA)

    cuadro = cubo.estado[cara.value] # nxn matriz de la cara
    # calcular tamano de cubitos para poder encajar todos en el frame
    dimension = len(cuadro)
    tamanoDeCubito = int(TAMANO_DE_CARA / dimension)

    for i in range(dimension):
        for j in range(dimension):
            # averiguar color
            texto = cuadro[i][j][0] # tomar primer carácter del texto
            color = COLORES_DE_CUBO[Cara[texto]] # convertir texto a Enum
            # dibujar cubito
            cubito = Frame(
                frame, 
                width=tamanoDeCubito, 
                height=tamanoDeCubito, 
                borderwidth=1,
                relief=SOLID,
                bg=color,
            )
            # meterlo a su posición determinada por la matriz de la que viene
            cubito.grid(row=i, column=j)

    return frame