# disable private member access warning
# pylint: disable=W0212

# disable warning for x == x
# pylint: disable=R0124

import unittest
import numpy as np

from models import cube
from constants.enums import Face

class TestCube(unittest.TestCase):
    def test_str_to_face_matrix(self):
        list_a = [['U', 'L'], ['B', 'D']]
        list_b = [['U', 'L'], ['32', '23'], ['D', 'R']]
        list_c = [['U', 'L', 'D'], ['D', 'F', 'R'], ['B', 'L', 2]]

        self.assertTrue(
            np.array_equal(cube._str_to_face_matrix(list_a),
            np.array([[Face.U, Face.L],[Face.B, Face.D]]))
        )

        self.assertRaises(ValueError, cube._str_to_face_matrix, list_b)
        self.assertRaises(KeyError, cube._str_to_face_matrix, list_c)

    # class methods

    def test_str(self):
        cubo_a = cube.Cube(
            u = np.array([[Face.U, Face.R], [Face.D, Face.B]]),
            d = np.array([[Face.U, Face.F], [Face.U, Face.U]]),
            f = np.array([[Face.B, Face.R], [Face.B, Face.D]]),
            b = np.array([[Face.D, Face.R], [Face.F, Face.F]]),
            l = np.array([[Face.B, Face.L], [Face.L, Face.L]]),
            r = np.array([[Face.D, Face.F], [Face.L, Face.R]]),
        )

        self.assertEqual(str(cubo_a),
            '\n'.join([
                '[U][R]', '[D][B]\n', # U
                '[U][F]', '[U][U]\n', # D
                '[B][R]', '[B][D]\n', # F
                '[D][R]', '[F][F]\n', # B
                '[B][L]', '[L][L]\n', # L
                '[D][F]', '[L][R]\n\n', # R    
            ])
        )

    def test_eq(self):
        x = cube.generate_cube(2)
        y = cube.generate_cube(2)
        z = cube.generate_cube(2)

        different_a = cube.generate_cube(3)
        different_b = cube.generate_cube(2)
        different_b.exec_algorithm(["U"])

        # Should be reflexive
        self.assertTrue(x == x)
        self.assertTrue(y == y)

        # Should be symmetric
        # Same
        self.assertTrue(x == y)
        self.assertTrue(y == x)
        # Different
        self.assertFalse(x == different_a)
        self.assertFalse(different_a == x)
        self.assertFalse(x == different_b)
        self.assertFalse(different_b == x)

        # Should be transitive
        # Same
        self.assertTrue(x == z)
        # Different
        self.assertFalse(different_a == z)
        self.assertFalse(different_b == z)

    def test_get_face(self):
        cube_a = cube.cube_from_str(
            u = [['U', 'D'], ['U', 'U']],
            d = [['R', 'D'], ['D', 'L']],
            f = [['F', 'F'], ['B', 'R']],
            b = [['F', 'B'], ['D', 'B']],
            l = [['L', 'L'], ['L', 'U']],
            r = [['R', 'R'], ['B', 'F']]
        )

        self.assertTrue(np.array_equal(cube_a.get_face(Face.U),
            np.array([[Face.U, Face.D], [Face.U, Face.U]])
        ))

        self.assertTrue(np.array_equal(cube_a.get_face(Face.R),
            np.array([[Face.R, Face.R], [Face.B, Face.F]])
        ))

    def test_set_face(self):
        cube_a = cube.generate_cube(2)

        l_face = np.array([[Face.F, Face.D], [Face.U, Face.U]])
        cube_a._set_face(Face.L, l_face)
        self.assertTrue(np.array_equal(cube_a.get_face(Face.L), l_face))

        b_face = np.array([[Face.U, Face.U], [Face.D, Face.B]])
        cube_a._set_face(Face.L, b_face)
        self.assertTrue(np.array_equal(cube_a.get_face(Face.L), b_face))

    # public methods

    def test_copy_cube(self):
        pass


    def test_cube_from_str(self):
        cube_a = cube.cube_from_str(
            u = [['U', 'D'], ['U', 'U']],
            d = [['R', 'D'], ['D', 'L']],
            f = [['F', 'F'], ['B', 'R']],
            b = [['F', 'B'], ['D', 'B']],
            l = [['L', 'L'], ['L', 'U']],
            r = [['R', 'R'], ['B', 'F']]
        )

        self.assertEqual(str(cube_a),
            '\n'.join([
                '[U][D]', '[U][U]\n', # U
                '[R][D]', '[D][L]\n', # D
                '[F][F]', '[B][R]\n', # F
                '[F][B]', '[D][B]\n', # B
                '[L][L]', '[L][U]\n', # L
                '[R][R]', '[B][F]\n\n', # R    
            ])
        )


    def test_generate_cube(self):
        cube_a = cube.generate_cube(2)
        cube_b = cube.generate_cube(3)

        self.assertEqual(str(cube_a),
            '\n'.join([
                '[U][U]', '[U][U]\n', # U
                '[D][D]', '[D][D]\n', # D
                '[F][F]', '[F][F]\n', # F
                '[B][B]', '[B][B]\n', # B
                '[L][L]', '[L][L]\n', # L
                '[R][R]', '[R][R]\n\n', # R    
            ])
        )
        self.assertEqual(str(cube_b),
            '\n'.join([
                '[U][U][U]', '[U][U][U]', '[U][U][U]\n', # U
                '[D][D][D]', '[D][D][D]', '[D][D][D]\n', # D
                '[F][F][F]', '[F][F][F]', '[F][F][F]\n', # F
                '[B][B][B]', '[B][B][B]', '[B][B][B]\n', # B
                '[L][L][L]', '[L][L][L]', '[L][L][L]\n', # L
                '[R][R][R]', '[R][R][R]', '[R][R][R]\n\n', # R
            ])
        )

    def test_reset(self):
        cube_a = cube.generate_cube(2)
        initial_cube_a = cube.copy_cube(cube_a)

        cube_a.exec_algorithm(["R", "U", "R'", "U'"])
        self.assertNotEqual(cube_a, initial_cube_a)

        cube_a.reset()
        self.assertEqual(cube_a, initial_cube_a)


    def test_is_solved(self):
        self.skipTest("Unimplemented")

        cube5x5 = cube.generate_cube(5)
        self.assertTrue(cube.is_solved(cube5x5))

        cube5x5.exec_algorithm(['U'])
        self.assertFalse(cube.is_solved(cube5x5))

        cube5x5.exec_algorithm(["U'", 'D', 'F2', 'B', "L'"])
        self.assertFalse(cube.is_solved(cube5x5))

        cube5x5.reset()
        self.assertTrue(cube.is_solved(cube5x5))

        # verify off-center cubes can be considered "solved"
        off_center = cube.cube_from_str(
            u = [['L', 'L'], ['L', 'L']],
            d = [['R', 'R'], ['R', 'R']],
            f = [['F', 'F'], ['F', 'F']],
            b = [['B', 'B'], ['B', 'B']],
            r = [['U', 'U'], ['U', 'U']],
            l = [['D', 'D'], ['D', 'D']],
        )
        self.assertTrue(cube.is_solved(off_center))

        unsolved = cube.cube_from_str(
            u = [['U', 'D'], ['U', 'U']],
            d = [['R', 'D'], ['D', 'L']],
            f = [['F', 'F'], ['B', 'R']],
            b = [['F', 'B'], ['D', 'B']],
            l = [['L', 'L'], ['L', 'U']],
            r = [['R', 'R'], ['B', 'F']]
        )
        self.assertFalse(cube.is_solved(unsolved))

if __name__ == '__main__':
    unittest.main()
