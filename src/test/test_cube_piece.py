# disable private member access warning
# pylint: disable=W0212

import unittest

from ursina import Entity, Ursina, color
from constants.enums import Face
from models import cube_piece as c

PINK = '#FFC0CB'
WHITE = '#FFFFFF'
GREEN = '#00FF00'

class TestCubePiece(unittest.TestCase):
    def test_create_plane(self):
        Ursina(window_type='none')
        entity = Entity()

        plane_a = c._create_plane(entity, Face.L, WHITE)
        self.assertEqual(plane_a.parent, entity)
        self.assertEqual(plane_a.origin_y, -0.5)
        self.assertEqual(plane_a.color_getter(), color.hex(WHITE))

        plane_b = c._create_plane(entity, Face.L, GREEN)
        self.assertEqual(plane_b.parent, entity)
        self.assertEqual(plane_b.origin_y, -0.5)
        self.assertEqual(plane_b.color_getter(), color.hex(GREEN))

    def test_set_color(self):
        Ursina(window_type='none')
        piece = c.CubePiece(0, 0, 0)

        self.assertNotEqual(
            piece.planes[Face.U].color_getter(),
            color.hex(PINK)
        )
        # change the color to pink
        piece.set_color(Face.U, PINK)
        self.assertEqual(
            piece.planes[Face.U].color_getter(),
            color.hex(PINK)
        )

        # try it again
        piece.set_color(Face.U, GREEN)
        self.assertEqual(
            piece.planes[Face.U].color_getter(),
            color.hex(GREEN)
        )
