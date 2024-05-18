from models.cube_piece import CubePiece
from models.cube import generate_cube
from constants.enums import Face
from constants.colors import CUBE_COLORS


class Cube3d:
    """
    Model representing a Rubik's cube in 3D utilizing the CubePiece class
    inherited from Ursina

    Must be used only after initiating an Ursina app
    """
    def __init__(self, dimension: int):
        self._dimension = dimension
        self._pieces = _generate_pieces(dimension)
        self._cube2d = generate_cube(dimension)

        self.cube2d.on_change(lambda: _paint_cube(self))

    @property
    def dimension(self):
        return self._dimension

    @property
    def pieces(self):
        return self._pieces

    @property
    def cube2d(self):
        return self._cube2d


def _is_border(x: int, y: int, z: int, dimension: int) -> bool:
    """
    Returns `True` if and only if the coordenates (x, y, z) are at a bordering
    edge of an NxNxN cube with dimension `dimension`
    """
    return (
        x in (0, dimension - 1)
        or y in (0, dimension - 1)
        or z in (0, dimension - 1)
    )


def _generate_pieces(dimension: int):
    """
    Create a 3d matrix for a Cube3d with Ursina entities
    """
    if dimension < 2:
        raise ValueError(f'Dimension must be at least 2: {dimension}')

    offset = - (dimension - 1) / 2  # TODO: make positive

    # create 3d matrix filled with `None`
    # the inner space is invisible but takes up the majority of the space,
    # it would be wasteful to put anything there
    pieces: list[list[list[CubePiece | None]]] = [
        [[None] * dimension for _ in range(dimension)] for _ in range(dimension)
    ]

    # fill cube edges with new cube pieces
    for x in range(dimension):
        for y in range(dimension):
            for z in range(dimension):
                if not _is_border(x, y, z, dimension):
                    continue

                pos_x = offset + x
                pos_y = offset + y
                pos_z = offset + z

                pieces[x][y][z] = CubePiece(pos_x, pos_y, pos_z)

    return pieces


def _get_piece(pieces: list[list[list[CubePiece | None]]], x: int, y: int, face: Face):
    """
    Returns a reference to the cube piece indicated by the 2d coordinates and
    origin face

    * `x` and `y` must be within the range 0 - len(pieces)
    """
    limit = len(pieces) - 1
    piece = None

    if face == Face.D:
        piece = pieces[x][0][y]
    elif face == Face.U:
        piece = pieces[x][limit][limit - y]
    elif face == Face.F:
        piece = pieces[x][limit - y][0]
    elif face == Face.B:
        piece = pieces[limit - x][limit - y][limit]
    elif face == Face.L:
        piece = pieces[0][limit - y][limit - x]
    elif face == Face.R:
        piece = pieces[limit][limit - y][x]

    if piece is None:
        raise ReferenceError('piece not found')

    return piece


def _paint_cube(cube: Cube3d):
    """
    Paint the entities of the given cube with the state of `cube.cube2d`
    * Modifies the color all cube pieces
    """
    state = cube.cube2d.state

    for face in Face:
        for y, row in enumerate(state[face]):
            for x, sticker in enumerate(row):
                color = CUBE_COLORS[sticker]
                piece = _get_piece(cube.pieces, x, y, face)
                piece.set_color(face, color)
