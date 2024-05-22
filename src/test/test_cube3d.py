# disable private member access warning
# pylint: disable=W0212
# pylint: disable=W0718

import unittest
from ursina import Ursina
from models import cube3d

class TestCube3d(unittest.TestCase):
    def test_generate_pieces(self):
        try:
            Ursina(window_type='None')
        except Exception as e:
            # instance already running
            print(e)

        dim = 3
        offset = -1

        pieces = cube3d._generate_pieces(dim)
        self.assertEqual(len(pieces), dim)

        for x, square in enumerate(pieces):
            # verify that the pieces are NxN
            self.assertEqual(len(square), dim)
            for y, row in enumerate(square):
                # verify that the pieces are NxNxN
                self.assertEqual(len(row), dim)
                for z, piece in enumerate(row):
                    is_border = (
                        x in (0, dim - 1)
                        or y in (0, dim - 1)
                        or z in (0, dim - 1)
                    )
                    if not is_border:
                        self.assertIsNone(piece)
                        continue

                    pos = piece.position_getter() # type: ignore

                    # verify that the position is the same as its indicies
                    self.assertEqual(pos.X, x + offset)
                    self.assertEqual(pos.Y, y + offset)
                    self.assertEqual(pos.Z, z + offset)
