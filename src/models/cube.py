from typing import Callable, Literal
from itertools import product
import copy
import numpy as np

from constants.enums import Face
from models.move import Move, text_to_move
import util.matrices as ma

class Cube:
    """
    Model representing a Rubik's cube with 6 faces.
    Not recommended to construct directly, 
    use `generate_cube` or `cube_from_str`

    The faces are:
    * U (up)
    * D (down)
    * F (front)
    * B (back)
    * L (left)
    * R (right)
    """

    def __init__(self, *,
            u: np.ndarray,
            d: np.ndarray,
            f: np.ndarray,
            b: np.ndarray,
            l: np.ndarray,
            r: np.ndarray
        ):
        # validate_faces(u, d, f, b, l, r)
        self._listeners = []

        self._dimension = len(u)
        if self._dimension < 2:
            raise ValueError(
                f'Dimension must be at least 2: (dimension = {self._dimension})')

        self._state = {
            Face.U: u,
            Face.D: d,
            Face.F: f,
            Face.B: b,
            Face.L: l,
            Face.R: r
        }
        # readonly variable
        self._initial_state = copy.deepcopy(self._state)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Cube):
            return False
        if __value._dimension != self._dimension:
            return False

        for face in Face:
            this_face = self.get_face(face)
            other_face = __value.get_face(face)
            if not np.array_equal(this_face, other_face):
                return False

        return True

    def __str__(self):
        result = ""
        for square in self._state.values():
            # nxn loop
            for row in square:
                for piece in row:
                    result += f'[{piece.value}]'
                result += '\n'
            result += '\n'

        return result


    # public methods

    @property
    def dimension(self):
        return self._dimension

    @property
    def state(self):
        return copy.deepcopy(self._state)

    def get_face(self, cara: Face):
        """Returns a copy of the specified face"""
        return copy.deepcopy(self._state[cara])

    def reset(self):
        """Reset the cube to its initial state"""
        self._state = copy.deepcopy(self._initial_state)
        self._notify_listeners()

    def exec_alg(self, alg: list[Move]):
        """
        Given a list of moves, performs every move on the cube
        """
        for move in alg:
            self.move(move)

    def exec_str_alg(self, alg: list[str]):
        """
        Given a list of string representations of movements,
        executes every movement on the cube.

        * requires that every element be a valid representation of a movement
        """

        # catch any encoding errors before execution
        parsed_alg = [text_to_move(move) for move in alg]
        self.exec_alg(parsed_alg)

    def move(self, mov: Move):
        if mov.depth == 1:
            # the face is only turned if level = 1
            turned_face = ma.rotate_matrix(self._state[mov.face], mov.direction)
            self._set_face(mov.face, turned_face)

        clockwise = bool(mov.direction == 1)
        direction = mov.direction
        line = mov.depth - 1
        if mov.face in [Face.D, Face.B, Face.R]:
            # this faces turn opposite to their reference order
            clockwise = not clockwise
            line = self._dimension - mov.depth
            # avoids -2 as a direction
            if direction != 2:
                direction = mov.direction * -1

        if mov.face in [Face.U, Face.D]:
            # horizontal faces
            self._state = ma.horizontal_slice(
                self._state, line, direction) # type: ignore
        elif mov.face in [Face.L, Face.R]:
            # vertical faces
            self._state = ma.vertical_slice(
                self._state, line, direction) # type: ignore
        else:
            # border faces (F, B)
            self._state = ma.border_slice(
                self._state, line, direction) # type: ignore

        self._notify_listeners()

    def on_change(self, callback: Callable):
        self._listeners.append(callback)


    # private methods

    def _set_face(self, cara: Face, matriz: np.ndarray):
        self._state[cara] = matriz

    def _notify_listeners(self):
        for callback in self._listeners:
            callback()


# other public utilities

def copy_cube(cubo: Cube):
    """
    Generate and return a deep copy of the passed in cube
    """
    return Cube(
        u = cubo.get_face(Face.U),
        d = cubo.get_face(Face.D),
        f = cubo.get_face(Face.F),
        b = cubo.get_face(Face.B),
        l = cubo.get_face(Face.L),
        r = cubo.get_face(Face.R),
    )


def cube_from_str(*,
            u: list[list[str]],
            d: list[list[str]],
            f: list[list[str]],
            b: list[list[str]],
            l: list[list[str]],
            r: list[list[str]]
        ):
    """
    Crear un cubo dado matrices de tipo str
    * requiere que cada str sea una Etiqueta válida

    Create a cube provided matricies for each face of type str
    * Requires that every string is a face: "U", "B", "F", "D", "R", "L",
    """
    return Cube(
        u = _str_to_face_matrix(u),
        d = _str_to_face_matrix(d),
        f = _str_to_face_matrix(f),
        b = _str_to_face_matrix(b),
        r = _str_to_face_matrix(r),
        l = _str_to_face_matrix(l),
    )


def generate_cube(dimension: int):
    """
    Returns an NxNxN solved cube of the given dimension
    - dimension: Must be at least 2
    """
    if dimension < 2:
        raise ValueError(
            f'Dimension must be at least 2: (dimension = {dimension})')

    faces = {}

    for f in Face:
        faces[f] = np.full((dimension, dimension), f)

    return Cube(
        u=faces[Face.U],
        d=faces[Face.D],
        f=faces[Face.F],
        b=faces[Face.B],
        l=faces[Face.L],
        r=faces[Face.R],
    )


# private helpers

def _str_to_face_matrix(matrix: list[list[str]]):
    """
    Given a matrix of strings, return a matrix of type `Face`.
    * Requires that every str entry maps to the `Face` enum type
    """
    dimension = len(matrix)
    result = np.full((dimension, dimension), None)

    # populate result with the mapping str -> Face
    for x, row in enumerate(matrix):
        if len(row) != dimension:
            raise ValueError('matrix is not NxN')
        for y, face_str in enumerate(row):
            result[x, y] = Face[face_str]

    return result


def is_solved(cube: Cube) -> bool:
    """Returns `True` if `cube` is solved, `False` otherwise"""
    faces_seen = set()

    for side in cube.state.values():
        sample = side[0, 0]
        # each side should have a unique color
        if sample in faces_seen:
            return False

        # check that every element is the same color
        if not np.all(side == sample):
            return False

        faces_seen.add(sample)

    # all 6 sides should have been seen
    return len(faces_seen) == len(Face)


# TODO
def find_optimal_solution(cube: Cube) -> list[Move]:
    """
    Find the shortest solution possible for the given cube,
    using breadth first search. This is quite slow (exponential time), consider
    running this in a seperate thread

    * Returns algorithm that solves the cube
    """
    # moveset = _generate_moveset(cube.dimension)
    # queue = []

    # while not optimal():
    #     current = queue.pop(0)

    #     for move in legal_moves():
    #         current.append(move)
    #         cube.exec_alg(current)
    #         if is_solved(cube):
    #             return current
    #         cube.reset()

    raise ReferenceError("Unimplemented: find_optimal_solution")


def _generate_moveset(dimension: int) -> set[Move]:
    """
    Returns a set of all possible moves for a cube of the given dimension
    """
    # typing needed to satisfy the type checker
    directions: list[Literal[-1, 1, 2]] = [-1, 1, 2]
    depth_range = range(1, (dimension // 2) + 1)
    widths = [True, False] if dimension > 2 else [False]

    combinations = product(Face, directions, depth_range, widths)

    return {
        Move(face, direction, depth, is_wide)
        for face, direction, depth, is_wide in combinations
    }
