import copy
import numpy as np

from constantes.enums import Cara

# el ciclo que siguen las caras al hacer el movimiento U
CARAS_HORIZONTALES = [Cara.F, Cara.L, Cara.B, Cara.R]

# el ciclo que siguen las caras al hacer el movimiento L
CARAS_VERTICALES = [Cara.F, Cara.D, Cara.B, Cara. U]

# el ciclo que siguen las caras al hacer el movimiento F
CARAS_FRONTERIZAS = [Cara.U,  Cara.R, Cara.D, Cara.L]

def girar_matriz_horario(matriz: np.ndarray):
    #return np.fliplr(matriz.transpose())
    return np.rot90(matriz, axes=(1, 0))


def girar_matriz_antihorario(matriz: np.ndarray):
    #return np.flipud(matriz.transpose())
    return np.rot90(matriz, axes=(0, 1))

def cotar_horizontalmente(estado_de_cubo: dict[Cara, np.ndarray], fila: int, horario: bool) -> dict[Cara, np.ndarray]:
    """
    rotar la capa en la fila espesificada horizontalmente.
    * Si horario = True, la rotación será horaria, Si no, será antihoraria
    * returns nuevo estado de cubo con la fila rotada
    """
    # la orden en la cual copiaremnos las caras horariamente
    orden = CARAS_HORIZONTALES
    if horario:
        # ponerla al revés para copiar antihorariamente
        orden = CARAS_HORIZONTALES[::-1]

    estado_nuevo = copy.deepcopy(estado_de_cubo)
    primera_fila = copy.deepcopy(estado_de_cubo[orden[0]][fila])

    # copiar filas en la orden dado para hacer una rotación
    for destino, fuente in zip(orden, orden[1:]):
        copia_de_fila = copy.deepcopy(estado_nuevo[fuente][fila])
        estado_nuevo[destino][fila] = copia_de_fila

    estado_nuevo[orden[-1]][fila] = primera_fila

    return estado_nuevo


def cotar_verticalmente(estado_de_cubo: dict[Cara, np.ndarray], columna: int, horario: bool) -> dict[Cara, np.ndarray]:
    """
    rotar la capa en la columna espesificada verticalmente.
    * Si horario = True, la rotación será horaria, Si no, será antihoraria
    * returns nuevo estado de cubo con la fila rotada
    """
    dimension = len(estado_de_cubo[Cara.U])
    # la orden en la cual copiaremnos las caras horariamente
    orden = CARAS_VERTICALES
    if horario:
        # ponerla al revés para copiar antihorariamente
        orden = CARAS_VERTICALES[::-1]

    estado_nuevo = copy.deepcopy(estado_de_cubo)
    primera_columna = copy.deepcopy(estado_de_cubo[orden[0]][0:, columna])

    # copiar filas en la orden dado para hacer una rotación
    for destino, fuente in zip(orden, orden[1:]):
        # copiar
        cara_fuente = estado_nuevo[fuente]
        if fuente == Cara.B:
            # la cara B es invertida a 180 degrados, necesitamos invertir
            # esta cara para compensar
            cara_fuente = np.rot90(cara_fuente, 2)
        copia_de_columna = copy.deepcopy(cara_fuente[0:, columna])

        # pegar
        columna_destino = columna
        if destino == Cara.B:
            # dado que la cara B es invertida, pegamos la columna al
            # lado opuesto e invertida
            columna_destino = dimension - columna - 1
            copia_de_columna = np.flipud(copia_de_columna)

        estado_nuevo[destino][0:, columna_destino] = copia_de_columna

    estado_nuevo[orden[-1]][0:, columna] = primera_columna

    return estado_nuevo
