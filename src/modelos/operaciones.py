from typing import Literal

import copy
import random
import numpy as np

from constantes.enums import Cara
from modelos.movimiento import Movimiento

# el ciclo que siguen las caras al hacer el movimiento U
CARAS_HORIZONTALES = [Cara.F, Cara.L, Cara.B, Cara.R]

# el ciclo que siguen las caras al hacer el movimiento L
CARAS_VERTICALES = [Cara.F, Cara.D, Cara.B, Cara. U]

# el ciclo que siguen las caras al hacer el movimiento F
# cada tuple representa (Cara, rotaciones necesarias antes de copiar)
CARAS_FRONTERIZAS = [(Cara.D, 0), (Cara. L, -1), (Cara.U, 2), (Cara.R, 1)]

# LONGITUD_DE_SCRAMBLES[dimensión] = # de movimientos,
# donde 2 <= dimensión <= 10
LONGITUD_DE_SCRAMBLES = [0, 0, 9, 25, 40, 60, 80, 90, 100, 110, 120]


def generar_scramble(dimension: int) -> list[Movimiento]:
    scramble = []

    for _ in range(_longitud_de_scramble(dimension)):
        if len(scramble) == 0:
            cara = random.choice(list(Cara))
        else:
            # hay que evitar a elegir la misma cara dos veces
            ultima_cara = scramble[-1].cara

            caras_disponibles = list(Cara)
            caras_disponibles.remove(ultima_cara)
            cara = random.choice(caras_disponibles)

        nivel = random.randint(1, dimension // 2)
        direccion: Literal[-1, 1, 2] = random.choice([-1, 1, 2])

        scramble.append(Movimiento(cara, direccion, nivel, False))

    return scramble


def girar_matriz(matriz: np.ndarray, orientacion: int):
    """
    Girar la matriz dada en sentido horario el número de veces dado como
    orientación
    """
    match orientacion % 4:
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
    return girar_matriz(matriz, -1)


def cotar_horizontalmente(
        estado_de_cubo: dict[Cara, np.ndarray], fila: int, direccion: int
    ) -> dict[Cara, np.ndarray]:
    """
    rotar la capa en la fila espesificada horizontalmente, dado la dirección en
    rotaciones en sentido horario
    * requiere 0 <= fila < dimensión de cubo
    * requiere que direccion sea -1, 1 o 2
    * returns nuevo estado de cubo con la fila rotada
    """
    if 0 > fila or fila >= len(estado_de_cubo[Cara.U]):
        raise ValueError('fila debe ser entre 0 - dimensión de cubo')
    if direccion not in [-1, 1, 2]:
        raise ValueError('direccion no es ni -1, ni 1, ni 2')

    # la orden en la cual copiaremnos las caras horariamente
    orden = CARAS_HORIZONTALES.copy()
    if direccion == 1:
        # ponerla al revés para copiar antihorariamente
        orden = CARAS_HORIZONTALES[::-1]

    estado_nuevo = copy.deepcopy(estado_de_cubo)
    primera_fila = copy.deepcopy(estado_de_cubo[orden[0]][fila])

    # copiar filas en la orden dado para hacer una rotación
    for destino, fuente in zip(orden, orden[1:]):
        copia_de_fila = copy.deepcopy(estado_nuevo[fuente][fila])
        estado_nuevo[destino][fila] = copia_de_fila

    estado_nuevo[orden[-1]][fila] = primera_fila

    if direccion == 2:
        # para un doble movimiento, haz dos movimientos primos
        return cotar_horizontalmente(estado_nuevo, fila, -1)

    return estado_nuevo


def cotar_verticalmente(
        estado_de_cubo: dict[Cara, np.ndarray], columna: int, direccion: int
    ) -> dict[Cara, np.ndarray]:
    """
    rotar la capa en la columna espesificada verticalmente.
    * Si horario = True, la rotación será horaria, Si no, será antihoraria
    * requiere 0 <= columna < dimensión de cubo
    * requiere que direccion sea -1, 1 o 2
    * returns nuevo estado de cubo con la fila rotada
    """
    if 0 > columna or columna >= len(estado_de_cubo[Cara.U]):
        raise ValueError('columna debe ser entre 0 - dimensión de cubo')
    if direccion not in [-1, 1, 2]:
        raise ValueError('direccion no es ni -1, ni 1, ni 2')

    dimension = len(estado_de_cubo[Cara.U])
    # la orden en la cual copiaremnos las caras horariamente
    orden = CARAS_VERTICALES.copy()
    if direccion == 1:
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

    if direccion == 2:
        # para un doble movimiento, haz dos movimientos primos
        return cotar_verticalmente(estado_nuevo, columna, -1)

    return estado_nuevo


def cortar_frontera(
        cubo_estado: dict[Cara, np.ndarray], linea: int, direccion: int
    ) -> dict[Cara, np.ndarray]:
    """
    rotar la capa por la frontera a la línea espesificada
    * Si horario = True, la rotación será horaria, Si no, será antihoraria
    * requiere 0 <= linea < dimensión de cubo
    * requiere que direccion sea -1, 1 o 2
    * returns nuevo estado de cubo con la frontera rotada
    """
    if 0 > linea or linea >= len(cubo_estado[Cara.U]):
        raise ValueError('frontera debe ser entre 0 - dimensión de cubo')
    if direccion not in [-1, 1, 2]:
        raise ValueError('direccion no es ni -1, ni 1, ni 2')

    # la orden en la cual copiaremnos las caras por la frontera
    orden = CARAS_FRONTERIZAS.copy()
    if direccion == 1:
        # ponerla al revés para copiar antihorariamente
        orden = CARAS_FRONTERIZAS[::-1]

    # la primera cara en orden es ignorada, entonces la agregamos al fin
    orden.append(orden[0])

    estado_nuevo = copy.deepcopy(cubo_estado)

    # copiar filas en la orden dado para hacer una rotación
    for destino, fuente in zip(orden, orden[1:]):
        cara_d = destino[0]
        orientacion_d = destino[1]
        orientacion_f = fuente[1]

        cara_f = girar_matriz(cubo_estado[fuente[0]], orientacion_f)
        copia_de_linea = copy.deepcopy(cara_f[linea])

        # girar la cara, pegar la línea, y girarla para atrás para
        # pegar la línea en la orientación que queremos
        estado_nuevo[cara_d] = girar_matriz(estado_nuevo[cara_d], orientacion_d)
        estado_nuevo[cara_d][linea] = copia_de_linea
        estado_nuevo[cara_d] = girar_matriz(estado_nuevo[cara_d], orientacion_d * -1)

    if direccion == 2:
        # para un doble movimiento, haz dos movimientos primos
        return cortar_frontera(estado_nuevo, linea, -1)

    return estado_nuevo


def _longitud_de_scramble(dimension: int):
    """
    Devuelve la longitud para un scramble de un como con la dimensión dada
    * requiere `dimension` >= 2
    """
    if dimension < 2:
        raise ValueError(f"La dimensión debe ser al menos 2: {dimension}")

    if dimension < len(LONGITUD_DE_SCRAMBLES):
        return LONGITUD_DE_SCRAMBLES[dimension]

    escalar_de_dim = 10
    compensacion = 20

    return (dimension * escalar_de_dim) + compensacion
