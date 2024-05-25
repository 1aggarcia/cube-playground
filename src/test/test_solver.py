import unittest
from models import cube
from util import solver


class TestSolver(unittest.TestCase):
    def test_find_optimal_solution(self):
        #self.skipTest("Unimplemented")

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

                sol = solver.find_optimal_solution(test_cube)
                print(f"optimal sol: {sol}")
                self.assertEqual(len(sol), exp_len)

                test_cube.exec_alg(sol)
                self.assertTrue(cube.is_solved(test_cube))

        test(cube.generate_cube(3), tests3x3)
        test(cube.generate_cube(2), tests2x2)

    def test_generate_moveset(self):
        expected2x2 = {
            'U', 'U2', "U'",
            'D', 'D2', "D'",
            'F', 'F2', "F'",
            'B', 'B2', "B'",
            'R', 'R2', "R'",
            'L', 'L2', "L'",
        }

        result2x2 = solver._generate_moveset(2)
        # convert to str since Moves don't hash correctly
        self.assertEqual(expected2x2, {str(m) for m in result2x2})

        expected3x3 = expected2x2
        # no support for wide moves yet
        # expected3x3 = {
        #     'U', 'U2', "U'", 'Uw', 'Uw2', "Uw'",
        #     'D', 'D2', "D'", 'Dw', 'Dw2', "Dw'",
        #     'F', 'F2', "F'", 'Fw', 'Fw2', "Fw'",
        #     'B', 'B2', "B'", 'Bw', 'Bw2', "Bw'",
        #     'R', 'R2', "R'", 'Rw', 'Rw2', "Rw'",
        #     'L', 'L2', "L'", 'Lw', 'Lw2', "Lw'",
        # }
        result3x3 = solver._generate_moveset(3)
        self.assertEqual(expected3x3, {str(m) for m in result3x3})

        expected6x6 = set(expected3x3)
        for move in expected3x3:
            expected6x6.add("2" + move)
            expected6x6.add("3" + move)

        result6x6 = solver._generate_moveset(6)
        self.assertEqual(expected6x6, {str(m) for m in result6x6})

if __name__ == '__main__':
    unittest.main()
