import copy
import numpy as np

from constantes.enums import Cara

# el ciclo que siguen las caras al hacer el movimiento U
CARAS_HORIZONTALES = [Cara.F, Cara.L, Cara.B, Cara.R]

# el ciclo que siguen las caras al hacer el movimiento L
CARAS_VERTICALES = [Cara.F, Cara.D, Cara.B, Cara. U]

# el ciclo que siguen las caras al hacer el movimiento F
CARAS_FRONTERIZAS = [(Cara. L, 3), (Cara.U, 2), (Cara.R, 1), (Cara.D, 0)]


def girar_matriz(matriz: np.ndarray, oriencacion: int):
    """
    Girar la matriz dada en sentido horario el número de veces dado como
    oriencación
    """
    match oriencacion % 4:
        case 0:
            # sin rotación
            return copy.deepcopy(matriz)
        case 1:
            # 90 degrados en sentido horario
            return np.rot90(matriz, axes=(1, 0))
        case 2:
            # 180 degrados
            return np.rot90(matriz, 2)
        case 3:
            # 90 degrados en sentio antihorario
            return np.rot90(matriz, axes=(0, 1))
        case _:
            raise RuntimeError('caso imposible')


def girar_matriz_horario(matriz: np.ndarray):
    return girar_matriz(matriz, 1)


def girar_matriz_antihorario(matriz: np.ndarray):
    return girar_matriz(matriz, 3)

def cotar_horizontalmente(
        estado_de_cubo: dict[Cara, np.ndarray], fila: int, horario: bool
    ) -> dict[Cara, np.ndarray]:
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


def cotar_verticalmente(
        estado_de_cubo: dict[Cara, np.ndarray], columna: int, horario: bool
    ) -> dict[Cara, np.ndarray]:
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
            cara_fuente = girar_matriz(cara_fuente, 2)
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


def cortar_frontera(
        estado_de_cubo: dict[Cara, np.ndarray], frontera: int, horario: bool
    ) -> dict[Cara, np.ndarray]:
    """
    rotar la capa de la frontera espesificada
    * Si horario = True, la rotación será horaria, Si no, será antihoraria
    * returns nuevo estado de cubo con la frontera rotada
    """
    # PSEUDOCÓDIGO
    #
    # orden = CARAS_FRONTERIZAS
    # if horario:
        # orden = al revés
    # orden.append(orden[0])
    #
    # estado_nuevo = copy.deepcopy(estado_de_cubo)
    #
    # for destino, fuente in orden:
        # cara_fuente = girar_matriz(estado_de_cubo, fuente.orientacion)
        # copia_de_linea = copy.deepcopy(cara_fuente[frontera])
        #
        # estado_nuevo[destino] = girar_matriz(estado_nuevo[destino], destino.orientacion)
        # estado_nuevo[destino][frontera] = copia_de_linea
        # estado_nuevo[destino] = girar_matriz(estado_nuevo[destino], destino.orientacion * -1)
    #
    # return estado_nuevo

    # para que el intérprete no se queje
    print(estado_de_cubo, frontera, horario)
    return {}
