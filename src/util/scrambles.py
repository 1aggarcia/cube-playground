from typing import Literal
import random

from constants.enums import Face
from models.move import Move

# SCAMBLE_LENGTHS[dimension] = # of turns
# where 2 <= dimension <= 10
SCAMBLE_LENGTHS = [0, 0, 9, 25, 40, 60, 80, 90, 100, 110, 120]


def generate_scramble(dimension: int) -> list[Move]:
    scramble = []

    for _ in range(_scramble_len(dimension)):
        if len(scramble) == 0:
            face = random.choice(list(Face))
        else:
            # avoid choosing the same face twice
            last_face = scramble[-1].face

            avail_faces = list(Face)
            avail_faces.remove(last_face)
            face = random.choice(avail_faces)

        depth = random.randint(1, dimension // 2)
        direction: Literal[-1, 1, 2] = random.choice([-1, 1, 2])

        scramble.append(Move(face, direction, depth, False))

    return scramble


def _scramble_len(dimension: int):
    """
    Return the length of a cube scramble for a cube with the passed in `dimension`
    * requires `dimension` >= 2
    """
    if dimension < 2:
        raise ValueError(f"dimension must be at least 2: {dimension}")

    if dimension < len(SCAMBLE_LENGTHS):
        return SCAMBLE_LENGTHS[dimension]

    dim_scale = 10
    compensation = 20

    return (dimension * dim_scale) + compensation
