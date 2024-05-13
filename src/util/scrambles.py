from typing import Literal
import random

from constants.enums import Cara
from models.move import Movimiento

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
