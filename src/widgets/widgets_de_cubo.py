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
    caraU = _crearFrameDeCara(frame, cubo, Cara.U)
    caraL = _crearFrameDeCara(frame, cubo, Cara.L)
    caraF = _crearFrameDeCara(frame, cubo, Cara.F)
    caraR = _crearFrameDeCara(frame, cubo, Cara.R)
    caraB = _crearFrameDeCara(frame, cubo, Cara.B)
    caraD = _crearFrameDeCara(frame, cubo, Cara.D)

    # posicionarlas para que se vean como un cubo plano
    caraU.grid(row=0, column=1)
    caraL.grid(row=1, column=0)
    caraF.grid(row=1, column=1)
    caraR.grid(row=1, column=2)
    caraB.grid(row=1, column=3)
    caraD.grid(row=2, column=1)

    return frame

def _crearFrameDeCara(raiz: Misc, cubo: Cubo, cara: Cara) -> Frame:
    '''
    Crea un frame representando la cara dada con una matriz de nxn cubitos,
    donde n = len(cara) indicado. Lo colora basado en el cubo dado.
    * returns frame con el nombre de la cara en minúscula con nxn niños colorados de tamaño igual
    '''
    frame = Frame(raiz, bg='black', name=cara.value.lower(),
                    width=TAMANO_DE_CARA, height=TAMANO_DE_CARA, padx=2, pady=2)
    
    # calcular tamaño de cubitos para poder encajar todos en el frame
    dimension = cubo.dimension
    tamanoDeCubito = int(TAMANO_DE_CARA / dimension)

    # llenar frame con los cubitos
    for i in range(dimension):
        for j in range(dimension):
            frameCubito = Frame(
                frame, 
                width=tamanoDeCubito, 
                height=tamanoDeCubito, 
                borderwidth=1,
                relief=SOLID,
            )       
            # meterlo a su posición determinada por la matriz de la que viene
            frameCubito.grid(row=i, column=j)

    return dibujarCara(frame, cubo, cara)

def dibujarCara(frame: Frame, cubo: Cubo, cara: Cara) -> Frame:
    '''
    Colora el frame dado con el cubo y la cara dada
    * requiere que el frame tiene nxn ninos Frame, donde n = len(cara) del cubo
    * returns mismo frame con los cubitos colorados
    '''
    dimension = cubo.dimension
    ninos = frame.winfo_children()
    if len(ninos) != dimension**2:
        raise ValueError('REQUISITO ROTO: frame dado no tiene nxn ninos')
    
    cuadro = cubo.estado[cara.value]
    
    for i in range(dimension):
        for j in range(dimension):
            # ninos es 1D, las caras son 2D.
            # El cubito [i][j] en 2D en una cara es lo mismo que
            # el cubito [i*dimension + j] in 1D
            cubito = ninos[i*dimension + j]
            color = COLORES_DE_CUBO[cuadro[i][j].cara]
            cubito.configure(bg=color)
    # for cubito in ninos:
    #     cubito.configure(bg=COLORES_DE_CUBO[cara])

    return frame

# def _dibujarCaraAnticuado(raiz: Misc, cubo: Cubo, cara: Cara):
#     frame = Frame(raiz, bg='black', name=cara.value.lower(),
#                    width=TAMANO_DE_CARA, height=TAMANO_DE_CARA, padx=2, pady=2)

#     cuadro = cubo.estado[cara.value] # nxn matriz de la cara

#     # calcular tamaño de cubitos para poder encajar todos en el frame
#     dimension = len(cuadro)
#     tamanoDeCubito = int(TAMANO_DE_CARA / dimension)

#     # llenar frame con los cubitos
#     for i in range(dimension):
#         for j in range(dimension):
#             # averiguar color
#             cubito = cuadro[i][j]
#             color = COLORES_DE_CUBO[cubito.cara]
#             # dibujar cubito
#             frameCubito = Frame(
#                 frame, 
#                 width=tamanoDeCubito, 
#                 height=tamanoDeCubito, 
#                 borderwidth=1,
#                 relief=SOLID,
#                 bg=color,
#             )
#             # meterlo a su posición determinada por la matriz de la que viene
#             frameCubito.grid(row=i, column=j)

#     return frame