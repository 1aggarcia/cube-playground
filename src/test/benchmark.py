# pylint: disable=W0212

"""Speed test for the solver module"""

import time
import json
from typing import Callable

from util import solver
from models.cube import Cube, generate_cube, is_solved
from models.move import Move


TEST_REPITITIONS = 10


def main():
    results = {}

    for i in range(TEST_REPITITIONS):
        run_tests(results)
        print(f'completed iteration {i + 1}')

    ordered_results = compile_results(results)
    print(json.dumps(ordered_results, indent=2))


def run_tests(results: dict):
    algs = [solver._list_impl, solver._queue_impl, solver._tree_impl]
    cube = generate_cube(3)

    scrambles = [['B'], ['F', 'U2'], ['L2', "F'", 'B']]

    for scramble in scrambles:
        for alg in algs:
            cube.exec_str_alg(scramble)
            (exec_time, sol) = time_alg(lambda: alg(cube))
            if not is_good_solution(cube, scramble, sol):
                raise ValueError(f'BAD SOLUTION FROM SOLVER {alg.__name__}')

            cube.reset()
            # print(f'{len(scramble)}: {exec_time}')
            alg_entry = results.get(alg.__name__, {})
            times = alg_entry.get(len(scramble), [])

            times.append(exec_time)
            alg_entry[len(scramble)] = times
            results[alg.__name__] = alg_entry


def compile_results(results: dict[str, dict[str, list]]):
    """
    Given a dictionary of algorithm benchark times,
    finds the average of each length of each algorithm,
    sorts the algorithms by longest average time

    Returns list of tuples of algorithms sorted by the
    longest average time
    """
    averaged = {}

    # Create a new dictionary out of the old one with
    # avergaged times
    for alg, scores in results.items():
        for length, seconds in scores.items():
            avg = sum(seconds) / len(seconds)

            alg_entry = averaged.get(alg, {})
            alg_entry[length] = avg

            averaged[alg] = alg_entry

    # key function for sorting
    def find_max_time(pair: tuple[str, dict[str, float]]):
        max_time = 0
        for _, seconds in pair[1].items():
            max_time = max(seconds, max_time)

        return max_time

    # Sort the averaged results
    ordered = list(averaged.items())
    ordered.sort(key=find_max_time)

    return ordered


def time_alg(func: Callable) -> tuple[float, list]:
    """
    Return a tuple of the execution time of the function, and the function's
    return value, as such: (time, ret_value)
    """
    start = time.perf_counter()
    ret_value = func()
    end = time.perf_counter()

    return (end - start, ret_value)


def is_good_solution(cube: Cube, scramble: list, sol: list[Move]):
    """
    Determine if a solution is good by two heuristics:
    1. The solution solves the cube
    2. The solution is no longer than the scramble

    Returns True if the two heuristics are met, False otherwise
    """
    cube.exec_alg(sol)
    if not is_solved(cube):
        cube.reset()
        return False

    cube.reset()
    return len(sol) <= len(scramble)


main()
