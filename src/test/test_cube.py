# disable private member access warning
# pylint: disable=W0212

# disable warning for x == x
# pylint: disable=R0124

import unittest
import numpy as np

from models import cube
from models.move import text_to_move
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
        different_b.exec_str_alg(["U"])

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

    def test_exec_alg(self):
        cube2x2 = cube.generate_cube(2)
        some_moves = [text_to_move(m) for m in ['R', 'U', "R'", "U'"]]

        cube2x2.exec_alg(some_moves)
        self.assertEqual(cube2x2,
            cube.cube_from_str(
                u = [['U', 'L'], ['U', 'F']],
                d = [['D', 'R'], ['D', 'D']],
                f = [['F', 'D'], ['F', 'F']],
                b = [['B', 'R'], ['B', 'B']],
                l = [['B', 'L'], ['L', 'L']],
                r = [['R', 'U'], ['U', 'R']]
            )
        )

        cube4x4 = cube.generate_cube(4)
        more_moves = [
            text_to_move(m) for m in ['D', "L'", 'D' ,"U'", '2B2', 'F2', '2D2']
        ]

        cube4x4.exec_alg(more_moves)
        self.assertEqual(cube4x4,
            cube.cube_from_str(
                u = [['U', 'U', 'U', 'U'],
                     ['D', 'D', 'D', 'D'],
                     ['U', 'U', 'U', 'U'],
                     ['R', 'B', 'B', 'B']],

                d = [['L', 'F', 'F', 'F'],
                     ['D', 'D', 'D', 'D'],
                     ['U', 'U', 'U', 'U'],
                     ['D', 'D', 'D', 'D']],

                f = [['B', 'L', 'L', 'L'],
                     ['F', 'F', 'F', 'D'],
                     ['B', 'B', 'B', 'U'],
                     ['B', 'L', 'L', 'L']],

                b = [['R', 'R', 'R', 'R'],
                     ['B', 'B', 'B', 'U'],
                     ['F', 'F', 'F', 'D'],
                     ['F', 'F', 'F', 'F']],

                l = [['B', 'L', 'B', 'D'],
                     ['L', 'R', 'L', 'R'],
                     ['B', 'R', 'L', 'R'],
                     ['R', 'F', 'R', 'D']],

                r = [['U', 'F', 'R', 'F'],
                     ['B', 'R', 'L', 'R'],
                     ['L', 'R', 'L', 'R'],
                     ['U', 'L', 'B', 'L']],
            )
        )

    def test_exec_str_alg(self):
        cube2x2 = cube.generate_cube(2)

        cube2x2.exec_str_alg(['R', 'U', "R'", "U'"])
        self.assertEqual(cube2x2,
            cube.cube_from_str(
                u = [['U', 'L'], ['U', 'F']],
                d = [['D', 'R'], ['D', 'D']],
                f = [['F', 'D'], ['F', 'F']],
                b = [['B', 'R'], ['B', 'B']],
                l = [['B', 'L'], ['L', 'L']],
                r = [['R', 'U'], ['U', 'R']]
            )
        )

        cube4x4 = cube.generate_cube(4)

        cube4x4.exec_str_alg(['D', "L'", 'D' ,"U'", '2B2', 'F2', '2D2'])
        self.assertEqual(cube4x4,
            cube.cube_from_str(
                u = [['U', 'U', 'U', 'U'],
                     ['D', 'D', 'D', 'D'],
                     ['U', 'U', 'U', 'U'],
                     ['R', 'B', 'B', 'B']],

                d = [['L', 'F', 'F', 'F'],
                     ['D', 'D', 'D', 'D'],
                     ['U', 'U', 'U', 'U'],
                     ['D', 'D', 'D', 'D']],

                f = [['B', 'L', 'L', 'L'],
                     ['F', 'F', 'F', 'D'],
                     ['B', 'B', 'B', 'U'],
                     ['B', 'L', 'L', 'L']],

                b = [['R', 'R', 'R', 'R'],
                     ['B', 'B', 'B', 'U'],
                     ['F', 'F', 'F', 'D'],
                     ['F', 'F', 'F', 'F']],

                l = [['B', 'L', 'B', 'D'],
                     ['L', 'R', 'L', 'R'],
                     ['B', 'R', 'L', 'R'],
                     ['R', 'F', 'R', 'D']],

                r = [['U', 'F', 'R', 'F'],
                     ['B', 'R', 'L', 'R'],
                     ['L', 'R', 'L', 'R'],
                     ['U', 'L', 'B', 'L']],
            )
        )

    # public functions

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

        cube_a.exec_str_alg(["R", "U", "R'", "U'"])
        self.assertNotEqual(cube_a, initial_cube_a)

        cube_a.reset()
        self.assertEqual(cube_a, initial_cube_a)


    def test_is_solved(self):
        cube5x5 = cube.generate_cube(5)
        self.assertTrue(cube.is_solved(cube5x5))

        cube5x5.exec_str_alg(['U'])
        self.assertFalse(cube.is_solved(cube5x5))

        cube5x5.exec_str_alg(["U'", 'D', 'F2', 'B', "L'"])
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

        # appears solved but there are two "U" faces
        duplicate_faces = cube.cube_from_str(
            u = [['U', 'U'], ['U', 'U']],
            d = [['U', 'U'], ['U', 'U']],
            f = [['F', 'F'], ['F', 'F']],
            b = [['B', 'B'], ['B', 'B']],
            l = [['L', 'L'], ['L', 'L']],
            r = [['R', 'R'], ['R', 'R']]
        )
        self.assertFalse(cube.is_solved(duplicate_faces))

    def test_find_optimal_solution(self):
        self.skipTest("Unimplemented")

        # two heuristics for correctness:
        # 1. algorithm must solve the cube
        # 2. algorithm must be the shortest possible

        # test cases formed as (scramble, optimal solution length)
        tests3x3 = [
            (["U'"], 1),
            (['L', 'B2'], 2)
        ]
        tests2x2 = [
            (['D2'],  1),
            (["U'", 'B'], 2)
        ]

        def test(test_cube: cube.Cube, cases: list[tuple[list[str], int]]):
            for (scramble, exp_len) in cases:
                test_cube.reset()
                test_cube.exec_str_alg(scramble)

                sol = cube.find_optimal_solution(test_cube)
                self.assertEqual(len(sol), exp_len)

                test_cube.exec_alg(sol)
                self.assertTrue(cube.is_solved(test_cube))

                print("!pass@\n")

        test(cube.generate_cube(3), tests3x3)
        test(cube.generate_cube(2), tests2x2)

if __name__ == '__main__':
    unittest.main()
