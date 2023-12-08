from tkinter import *

from modelos.cubo import Cubo
from constantes.colores import *

TAMANO_DE_CARA = 100 # ancho y altura de una cara

def crearLabelCubo(raiz: Misc, cubo: Cubo):
    return Label(raiz, text=str(cubo), bg=VERDE_2, fg='#ffffff')

def crearButtonCubo(raiz: Misc, callback):
    return Button(raiz, text='un botón', command=callback)

def crearFrameCubo(raiz: Misc, cubo: Cubo):
    frame = Frame(raiz, bg=VERDE_2)

    # crear widgets para cada cara
    caraU = _dibujarCara(frame, cubo, Cara.U)
    caraL = _dibujarCara(frame, cubo, Cara.L)
    caraF = _dibujarCara(frame, cubo, Cara.F)
    caraR = _dibujarCara(frame, cubo, Cara.R)
    caraB = _dibujarCara(frame, cubo, Cara.B)
    caraD = _dibujarCara(frame, cubo, Cara.D)

    # posicionarlas para que se vean como un cubo plano
    caraU.grid(row=0, column=1)
    caraL.grid(row=1, column=0)
    caraF.grid(row=1, column=1)
    caraR.grid(row=1, column=2)
    caraB.grid(row=1, column=3)
    caraD.grid(row=2, column=1)

    return frame

def _dibujarCara(raiz: Misc, cubo: Cubo, cara: Cara):
    frame = Frame(raiz, bg='black',
                   width=TAMANO_DE_CARA, height=TAMANO_DE_CARA, padx=2, pady=2)

    cuadro = cubo.estado[cara.value] # nxn matriz de la cara

    # calcular tamaño de cubitos para poder encajar todos en el frame
    dimension = len(cuadro)
    tamanoDeCubito = int(TAMANO_DE_CARA / dimension)

    # llenar frame con los cubitos
    for i in range(dimension):
        for j in range(dimension):
            # averiguar color
            cubito = cuadro[i][j]
            color = COLORES_DE_CUBO[cubito.cara]
            # dibujar cubito
            frameCubito = Frame(
                frame, 
                width=tamanoDeCubito, 
                height=tamanoDeCubito, 
                borderwidth=1,
                relief=SOLID,
                bg=color,
            )
            # meterlo a su posición determinada por la matriz de la que viene
            frameCubito.grid(row=i, column=j)

    return frame