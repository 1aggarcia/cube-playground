from tkinter import *

from modelos.cubo import Cubo
from constantes.colores import *

TAMANO_DE_CARA = 100 # ancho y altura de una cara

# métodos públicos

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

def colorarCubo(frame: Frame, cubo: Cubo) -> None:
    '''
    Colora el frame dado con el cubo dado
    * requiere que el frame tiene 6 niños con los nombres'u', 'd', 'l', 'r', 'f', 'b'
    * requiere que cada nino del frame sea un Frame con nxn ninos Frame,
        donde n = dimension del cubo
    * modifica el frame dado, colora todos los cubitos
    '''
    for cara in list(Cara):
        # chequear requisito 1
        try:
            cuadro = frame.nametowidget(cara.value.lower())
        except KeyError:
            raise ValueError(f'REQUISITO ROTO: los ninos de frame tiene nombres incorrectos')
        finally:
            # esta función chequea requisito 2
            # y modifica el cuadro
            _colorarCara(cuadro, cubo, cara)

# métodos privados

def _crearFrameDeCara(raiz: Misc, cubo: Cubo, cara: Cara) -> Frame:
    '''
    Crea un frame representando la cara dada con una matriz de nxn cubitos,
    donde n = len(cara) indicado. Lo colora basado en el cubo dado.
    * returns frame con el nombre de la cara en minúscula con nxn niños colorados de tamaño igual
    '''   
    # calcular tamaño de cubitos para poder encajar todos en el frame
    dimension = cubo.dimension
    tamanoDeCubito = int(TAMANO_DE_CARA / dimension)

    # crear frame central
    frame = Frame(raiz, bg='black', name=cara.value.lower(),
                    width=TAMANO_DE_CARA, height=TAMANO_DE_CARA, padx=2, pady=2)

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

    # colora el frame antes de devolverla
    _colorarCara(frame, cubo, cara)
    return frame

def _colorarCara(frame: Frame, cubo: Cubo, cara: Cara) -> None:
    '''
    Colora el frame dado con el cubo y la cara dada
    * requiere que el frame tiene nxn ninos Frame, donde n = dimension del cubo
    * modifica el frame dado, lo colora los cubitos
    '''
    dimension = cubo.dimension
    ninos = frame.winfo_children()
    if len(ninos) != dimension**2:
        raise ValueError('REQUISITO ROTO: frame dado no tiene nxn ninos')
    
    cuadro = cubo.getCara(cara)
    
    for i in range(dimension):
        for j in range(dimension):
            # ninos es 1D, las caras son 2D.
            # El cubito [i][j] en 2D en una cara es lo mismo que
            # el cubito [i*dimension + j] in 1D
            cubito = ninos[i*dimension + j]
            color = COLORES_DE_CUBO[cuadro[i][j].cara]
            # la modificación
            cubito.configure(bg=color)