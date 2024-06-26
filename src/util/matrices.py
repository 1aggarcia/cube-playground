import copy
from typing import Literal
import numpy as np

from constants.enums import Face

# the cycle that the faces follow on a U move
HORIZONTAL_CYCLE = [Face.F, Face.L, Face.B, Face.R]

# the cycle that the faces follow on an L move
VERTICAL_CYCLE = [Face.F, Face.D, Face.B, Face. U]

# the cycle that the faces follow on an F move
# each tuple represents (Face, needed rotation before copying)
BORDER_CYCLE = [(Face.D, 0), (Face. L, -1), (Face.U, 2), (Face.R, 1)]


def rotate_matrix(matrix: np.ndarray, repetitions: int):
    """
    Rotate and return the given matrix clockwise `repetitions` times
    """
    match repetitions % 4:
        case 0:
            # no rotation
            return copy.deepcopy(matrix)
        case 1:
            # 90 degrees clockwise
            return np.rot90(matrix, axes=(1, 0))
        case 2:
            # 180 degrees
            return np.rot90(matrix, 2)
        case 3:
            # 90 degrees counterclockwise
            return np.rot90(matrix, axes=(0, 1))
        case _:
            raise RuntimeError('impossible case')


def rotate_matrix_clockwise(matriz: np.ndarray):
    return rotate_matrix(matriz, 1)


def rotate_matrix_ccw(matriz: np.ndarray):
    return rotate_matrix(matriz, -1)


def horizontal_slice(
        cube_state: dict[Face, np.ndarray],
        row: int,
        direction: Literal[-1, 1, 2]
    ) -> dict[Face, np.ndarray]:
    """
    rotate the layer in the specified row horizontally, given the direction in
    clockwise rotations
    * requires 0 <= row <= cube dimension
    * returns new state with the rotated row
    """
    if 0 > row or row >= len(cube_state[Face.U]):
        raise ValueError('row must be between 0 - cube dimension')

    # the order the faces will be copied in (reversed for inverted move)
    order = HORIZONTAL_CYCLE[::-1] if direction == 1 else HORIZONTAL_CYCLE.copy()
    # the first face in the cycle is ignored, so it's copied to the end
    order.append(order[0])

    new_state = copy.deepcopy(cube_state)

    # copy the rows cyclicly in the given order to rotate
    for dst, src in zip(order, order[1:]):
        row_copy = copy.deepcopy(cube_state[src][row])
        new_state[dst][row] = row_copy

    if direction == 2:
        # for a double turn, do two prime turns
        return horizontal_slice(new_state, row, -1)

    return new_state


def vertical_slice(
        cube_state: dict[Face, np.ndarray],
        col: int,
        direction: Literal[-1, 1, 2]
    ) -> dict[Face, np.ndarray]:
    """
    rotates the layer in the specified column vertically.
    * Requires 0 <= col < cube dimension
    * Returns new cube state with the column rotated
    """
    if 0 > col or col >= len(cube_state[Face.U]):
        raise ValueError('col must be between 0 - cube dimension')

    dimension = len(cube_state[Face.U])
    order = VERTICAL_CYCLE[::-1] if direction == 1 else VERTICAL_CYCLE.copy()
    # the first face in the cycle is ignored, so it's copied to the end
    order.append(order[0])

    new_state = copy.deepcopy(cube_state)

    # copy columns in the given order to do a rotation
    for dst, src in zip(order, order[1:]):
        # copy
        src_face = cube_state[src]
        if src == Face.B:
            # Face B is inverted by 180 degrees, must be inverted back
            src_face = rotate_matrix(src_face, 2)
        col_copy = copy.deepcopy(src_face[0:, col])

        # paste
        dst_col = col
        if dst == Face.B:
            # since B is inverted, the paste location also must be inverted
            dst_col = dimension - col - 1
            col_copy = np.flipud(col_copy)

        new_state[dst][0:, dst_col] = col_copy

    if direction == 2:
        # for a double turn, do two prime turns
        return vertical_slice(new_state, col, -1)

    return new_state


def border_slice(
        cube_state: dict[Face, np.ndarray],
        line: int,
        direction: Literal[-1, 1, 2]
    ) -> dict[Face, np.ndarray]:
    """
    rotates the layer by the border at the specified "line"
    * Requires 0 <= col < cube dimension
    * Returns new cube state with the border line rotated
    """
    if 0 > line or line >= len(cube_state[Face.U]):
        raise ValueError('line must be between 0 - cube dimension')

    # cycle to follow for copying
    order = BORDER_CYCLE[::-1] if direction == 1 else BORDER_CYCLE.copy()
    # the first face in the cycle is ignored, so it's copied to the end
    order.append(order[0])

    new_state = copy.deepcopy(cube_state)

    for dst, src in zip(order, order[1:]):
        (dst_face, dst_orientation) = dst

        src_orientation = src[1]
        src_face = rotate_matrix(cube_state[src[0]], src_orientation)

        line_copy = copy.deepcopy(src_face[line])

        # rotate the face, paste the line, rotate it back
        # to paste the line in the correct orientation
        new_state[dst_face] = rotate_matrix(new_state[dst_face], dst_orientation)
        new_state[dst_face][line] = line_copy
        new_state[dst_face] = rotate_matrix(new_state[dst_face], dst_orientation * -1)

    if direction == 2:
        # for double turns
        return border_slice(new_state, line, -1)

    return new_state
