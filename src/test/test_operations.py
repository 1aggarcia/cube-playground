# pylint: disable=W0212

import unittest
import numpy as np

from models.cube import cube_from_str
from constants.enums import Face
import util.matrices as ma
import util.scrambles as sc


class TestOperations(unittest.TestCase):
    def test_generate_scramble(self):
        # 2x2
        scramble = sc.generate_scramble(2)

        self.assertEqual(sc._scramble_len(2), len(scramble))
        for mov_a, mov_b in zip(scramble, scramble[1:]):
            self.assertNotEqual(mov_a.face, mov_b.face)

        # 4x4
        scramble = sc.generate_scramble(4)

        self.assertEqual(sc._scramble_len(4), len(scramble))
        for mov_a, mov_b in zip(scramble, scramble[1:]):
            self.assertNotEqual(mov_a.face, mov_b.face)

    def test_rotate_matrix(self):
        # 90 degrees (clockwise)
        list_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        expected_a = np.array([
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])
        self.assertTrue(np.array_equal(expected_a, ma.rotate_matrix(list_a, 1)))

        list_b = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        expected_b = np.array([
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])
        self.assertTrue(np.array_equal(expected_b, ma.rotate_matrix(list_b, 1)))

        # 270 degrees (counter-clockwise)
        list_c = np.array(
            [[234, 123],
             [65, 2],
             [1, 2]]
        )
        expected_c = np.array([
            [123, 2, 2],
            [234, 65, 1]
        ])
        self.assertTrue(np.array_equal(expected_c, ma.rotate_matrix(list_c, 3)))

        list_d = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        expected_d = np.array([
            [4, 8, 12, 16],
            [3, 7, 11, 15],
            [2, 6, 10, 14],
            [1, 5, 9, 13]
        ])
        self.assertTrue(np.array_equal(expected_d, ma.rotate_matrix(list_d, 3)))

    def test_horizontal_slice(self):
        cube_a = cube_from_str(
            u = [['B', 'U'], ['U', 'D']],
            d = [['D', 'R'], ['U', 'D']],
            f = [['F', 'R'], ['F', 'B']],
            b = [['R', 'L'], ['L', 'B']],
            l = [['U', 'L'], ['R', 'L']],
            r = [['F', 'F'], ['D', 'B']]
        )
        result_a = ma.horizontal_slice(cube_a.state, 0, 1)
        expected_a = {
            Face.F: np.array([[Face.F, Face.F], [Face.F, Face.B]]),
            Face.L: np.array([[Face.F, Face.R], [Face.R, Face.L]]),
            Face.B: np.array([[Face.U, Face.L], [Face.L, Face.B]]),
            Face.R: np.array([[Face.R, Face.L], [Face.D, Face.B]]),
            Face.U: cube_a.get_face(Face.U),
            Face.D: cube_a.get_face(Face.D),
        }

        for face in Face:
            self.assertTrue(np.array_equal(result_a[face],
                                           expected_a[face]))

        result_b = ma.horizontal_slice(cube_a.state, 1, -1)
        expected_b = {
            Face.R: np.array([[Face.F, Face.F], [Face.F, Face.B]]),
            Face.F: np.array([[Face.F, Face.R], [Face.R, Face.L]]),
            Face.L: np.array([[Face.U, Face.L], [Face.L, Face.B]]),
            Face.B: np.array([[Face.R, Face.L], [Face.D, Face.B]]),
            Face.U: cube_a.get_face(Face.U),
            Face.D: cube_a.get_face(Face.D),
        }

        for face in Face:
            self.assertTrue(np.array_equal(result_b[face],
                                           expected_b[face]))

        result_c = ma.horizontal_slice(cube_a.state, 0, 2)
        expected_c = {
            Face.F: np.array([[Face.R, Face.L], [Face.F, Face.B]]),
            Face.B: np.array([[Face.F, Face.R], [Face.L, Face.B]]),
            Face.L: np.array([[Face.F, Face.F], [Face.R, Face.L]]),
            Face.R: np.array([[Face.U, Face.L], [Face.D, Face.B]]),
            Face.U: cube_a.get_face(Face.U),
            Face.D: cube_a.get_face(Face.D),
        }

        for face in Face:
            self.assertTrue(np.array_equal(result_c[face],
                                           expected_c[face]))

    def test_vertical_slice(self):
        cube_a = cube_from_str(
            u = [['B', 'U'], ['U', 'D']],
            d = [['D', 'R'], ['U', 'D']],
            f = [['F', 'R'], ['F', 'B']],
            b = [['R', 'L'], ['L', 'B']],
            l = [['U', 'L'], ['R', 'L']],
            r = [['F', 'F'], ['D', 'B']]
        )
        result_a = ma.vertical_slice(cube_a.state, 0, -1)
        expected_a = {
            Face.F: np.array([[Face.D, Face.R], [Face.U, Face.B]]),
            Face.U: np.array([[Face.F, Face.U], [Face.F, Face.D]]),
            Face.B: np.array([[Face.R, Face.U], [Face.L, Face.B]]),
            Face.D: np.array([[Face.B, Face.R], [Face.L, Face.D]]),
            Face.R: cube_a.get_face(Face.R),
            Face.L: cube_a.get_face(Face.L),
        }

        for face in Face:
            self.assertTrue(np.array_equal(result_a[face],
                                           expected_a[face]))

        result_b = ma.vertical_slice(cube_a.state, 1, 1)
        expected_b = {
            Face.U: np.array([[Face.B, Face.L], [Face.U, Face.R]]),
            Face.B: np.array([[Face.D, Face.L], [Face.R, Face.B]]),
            Face.D: np.array([[Face.D, Face.R], [Face.U, Face.B]]),
            Face.F: np.array([[Face.F, Face.U], [Face.F, Face.D]]),
            Face.R: cube_a.get_face(Face.R),
            Face.L: cube_a.get_face(Face.L),
        }

        for face in Face:
            self.assertTrue(np.array_equal(result_b[face],
                                           expected_b[face]))

        result_c = ma.vertical_slice(cube_a.state, 0, 2)
        expected_c = {
            Face.U: np.array([[Face.D, Face.U], [Face.U, Face.D]]),
            Face.D: np.array([[Face.B, Face.R], [Face.U, Face.D]]),
            Face.F: np.array([[Face.B, Face.R], [Face.L, Face.B]]),
            Face.B: np.array([[Face.R, Face.F], [Face.L, Face.F]]),
            Face.R: cube_a.get_face(Face.R),
            Face.L: cube_a.get_face(Face.L),
        }

        for face in Face:
            self.assertTrue(np.array_equal(result_c[face],
                                           expected_c[face]))

    def test_border_slize(self):
        cube_a = cube_from_str(
            u = [['D', 'L'], ['U', 'U']],
            d = [['D', 'R'], ['U', 'D']],
            f = [['F', 'R'], ['L', 'D']],
            b = [['B', 'B'], ['F', 'R']],
            l = [['R', 'L'], ['F', 'B']],
            r = [['B', 'U'], ['F', 'L']]
        )
        result_a = ma.border_slice(cube_a.state, 0, 1)
        expected_a = {
            Face.L: np.array([[Face.R, Face.D], [Face.F, Face.R]]),
            Face.U: np.array([[Face.D, Face.L], [Face.B, Face.L]]),
            Face.R: np.array([[Face.U, Face.U], [Face.U, Face.L]]),
            Face.D: np.array([[Face.F, Face.B], [Face.U, Face.D]]),
            Face.F: cube_a.get_face(Face.F),
            Face.B: cube_a.get_face(Face.B),
        }

        for face in Face:
            self.assertTrue(np.array_equal(result_a[face],
                                           expected_a[face]))

        result_b = ma.border_slice(cube_a.state, 1, -1)
        expected_b = {
            Face.D: np.array([[Face.D, Face.R], [Face.R, Face.F]]),
            Face.L: np.array([[Face.L, Face.L], [Face.D, Face.B]]),
            Face.U: np.array([[Face.U, Face.L], [Face.U, Face.U]]),
            Face.R: np.array([[Face.B, Face.D], [Face.F, Face.U]]),
            Face.F: cube_a.get_face(Face.F),
            Face.B: cube_a.get_face(Face.B),
        }

        for face in Face:
            self.assertTrue(np.array_equal(result_b[face],
                                           expected_b[face]))

        result_c = ma.border_slice(cube_a.state, 0, 2)
        expected_c = {
            Face.U: np.array([[Face.D, Face.L], [Face.R, Face.D]]),
            Face.D: np.array([[Face.U, Face.U], [Face.U, Face.D]]),
            Face.L: np.array([[Face.R, Face.F], [Face.F, Face.B]]),
            Face.R: np.array([[Face.B, Face.U], [Face.L, Face.L]]),
            Face.F: cube_a.get_face(Face.F),
            Face.B: cube_a.get_face(Face.B),
        }

        for face in Face:
            self.assertTrue(np.array_equal(result_c[face],
                                           expected_c[face]))

    def test_scramble_len(self):
        for i, v in enumerate(sc.SCAMBLE_LENGTHS[2:], start=2):
            self.assertEqual(v, sc._scramble_len(i))

        self.assertEqual(130, sc._scramble_len(11))
        self.assertEqual(510, sc._scramble_len(49))


if __name__ == '__main__':
    unittest.main()
