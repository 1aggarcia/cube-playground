# disable x == x warning
# pylint: disable=R0124

import unittest

import models.move as mv
from constants.enums import Face

class TestMove(unittest.TestCase):

    def test_eq(self):
        x = mv.Move(Face.D, 1, 1, False)
        y = mv.Move(Face.D, 1, 1, False)
        z = mv.Move(Face.D, 1, 1, False)
        different = mv.Move(Face.U, 2, 4, True)

        # Reflexivity
        self.assertTrue(x == x)
        self.assertTrue(y == y)

        # Symmetry
        # Same
        self.assertTrue(x == y)
        self.assertTrue(y == x)
        # Different
        self.assertFalse(x == different)
        self.assertFalse(different == x)

        # Transitivity
        self.assertTrue(x == z)
        self.assertFalse(different == z)

    def test_str(self):
        # depth = 1
        short_move = mv.Move(Face.U, 1, 1, False)
        self.assertEqual(str(short_move), "U")

        inv_move = mv.Move(Face.D, -1, 1, False)
        self.assertEqual(str(inv_move), "D'")

        double_move = mv.Move(Face.B, 2, 1, False)
        self.assertEqual(str(double_move), "B2")

        # depth = 1 & wide
        wide_move = mv.Move(Face.U, 1, 1, True)
        self.assertEqual(str(wide_move), "Uw")

        wide_inv_move = mv.Move(Face.D, -1, 1, True)
        self.assertEqual(str(wide_inv_move), "Dw'")

        wide_double_move = mv.Move(Face.B, 2, 1, True)
        self.assertEqual(str(wide_double_move), "Bw2")

        # depth > 1
        large_move = mv.Move(Face.U, 1, 2, False)
        self.assertEqual(str(large_move), "2U")

        large_inv_move = mv.Move(Face.D, -1, 3, False)
        self.assertEqual(str(large_inv_move), "3D'")

        large_double_move = mv.Move(Face.B, 2, 99, False)
        self.assertEqual(str(large_double_move), "99B2")

        # depth > 1 & wide
        large_wide_move = mv.Move(Face.U, 1, 34, True)
        self.assertEqual(str(large_wide_move), "34Uw")

        large_wide_inv_move = mv.Move(Face.D, -1, 4, True)
        self.assertEqual(str(large_wide_inv_move), "4Dw'")

        large_wide_double_move = mv.Move(Face.B, 2, 2, True)
        self.assertEqual(str(large_wide_double_move), "2Bw2")

    def test_text_to_move(self):
        # NO DEPTH
        # len = 1
        self.assertEqual(
            mv.text_to_move('U'),
            mv.Move(Face.U, 1, 1, False)
        )

        # len = 2: Uw, U', U2
        self.assertEqual(
            mv.text_to_move('Dw'),
            mv.Move(Face.D, 1, 1, True)
        )
        self.assertEqual(
            mv.text_to_move("L'"),
            mv.Move(Face.L, -1, 1, False)
        )
        self.assertEqual(
            mv.text_to_move('R2'),
            mv.Move(Face.R, 2, 1, False)
        )

        # len = 3: Uw', Uw2
        self.assertEqual(
            mv.text_to_move("Dw'"),
            mv.Move(Face.D, -1, 1, True)
        )
        self.assertEqual(
            mv.text_to_move('Rw2'),
            mv.Move(Face.R, 2, 1, True)
        )

        # WITH DEPTH
        # len = n + 1: 99U
        self.assertEqual(
            mv.text_to_move('99U'),
            mv.Move(Face.U, 1, 99, False)
        )

        # len = n + 2: 4Uw, 99U', 99U2
        self.assertEqual(
            mv.text_to_move('4Dw'),
            mv.Move(Face.D, 1, 4, True)
        )
        self.assertEqual(
            mv.text_to_move("22B'"),
            mv.Move(Face.B, -1, 22, False)
        )
        self.assertEqual(
            mv.text_to_move('4L2'),
            mv.Move(Face.L, 2, 4, False)
        )

        # len = n + 3: 99Uw', 99Uw2
        self.assertEqual(
            mv.text_to_move("5923Fw'"),
            mv.Move(Face.F, -1, 5923, True)
        )
        self.assertEqual(
            mv.text_to_move('5Uw2'),
            mv.Move(Face.U, 2, 5, True)
        )

    def test_invert_move(self):
        move_a = mv.Move(Face.D, 1, 1, True)
        expected = mv.Move(Face.D, -1, 1, True)

        self.assertEqual(expected, mv.invert_move(move_a))
        self.assertEqual(move_a, mv.invert_move(expected))

        move_b = mv.Move(Face.F, 2, 32, False)

        self.assertEqual(move_b, mv.invert_move(move_b))
