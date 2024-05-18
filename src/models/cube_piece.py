from copy import deepcopy
from ursina import Entity, Vec3

from constants.enums import Face
from constants.colors import CUBE_COLORS
from constants.cubes import FACE_VECTORS


class CubePiece(Entity):
    """
    Model for a piece of Rubik's cube for an Ursina app.
    Must be used after creation of an Ursina app.

    Has six sides with distinct colors that can be recolored,
    and a mutable position
    """
    def __init__(self, x: float, y: float, z: float):
        super().__init__()

        self.position = Vec3(x, y, z)
        self._planes = {
            cara: _create_plane(self, cara, CUBE_COLORS[cara])
            for cara in Face
        }

    @property
    def planes(self):
        return deepcopy(self._planes)

    def set_color(self, side: Face, hex_color: str):
        """
        Change the color of the side specified

        - side: The side of the piece to recolor
        - hex_color: The new color as a hex string
        """
        plane = self._planes[side]
        plane.color_setter(hex_color)


def _create_plane(root: Entity, face: Face, color: str):
    """
    Attach a new plane to the given entity

    - root: Entity to attach plane to
    - face: The side of the piece to attach the plane
    - color: The color of the plane

    Returns the new plane
    """
    plane = Entity(
        parent = root,
        model = 'plane',
        texture = 'white_cube',
        color = color,
        origin_y = -0.5
    )
    plane.look_at(FACE_VECTORS[face], 'up')

    return plane
