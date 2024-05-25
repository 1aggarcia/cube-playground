from typing import Literal
from dataclasses import dataclass
from itertools import product

from constants.enums import Face
from models.cube import Cube, copy_cube, is_solved
from models.move import Move


@dataclass
class MoveNode:
    move: Move
    parent: 'MoveNode | None'


def find_optimal_solution(cube: Cube) -> list[Move]:
    """
    Find the shortest solution possible for the given cube,
    using breadth first search. This is quite slow (exponential time), consider
    running this in a seperate thread

    * Returns algorithm that solves the cube
    """
    return _list_impl(cube)


def _list_impl(cube: Cube):
    # stores a list of possible algorithms
    test_cube = copy_cube(cube)
    moveset = _generate_moveset(cube.dimension)
    queue: list[list[Move]] = [[]]

    while not is_solved(cube):
        current = queue.pop(0)

        for move in moveset:
            if len(current) > 0 and move.face == current[-1].face:
                continue

            new_alg = current + [move]
            queue.append(new_alg)

            test_cube.reset()
            test_cube.exec_alg(new_alg)
            if is_solved(test_cube):
                print(f"Moves: {len(new_alg)}; Search space: {len(queue):,}")
                return new_alg

    print(f"Moves: {len(new_alg)}; Search space: {len(queue):,}")
    return queue[-1]


def _tree_impl(cube: Cube):
    # creates a tree of all moves to reduce memory usage
    # somehow 3x slower?
    test_cube = copy_cube(cube)
    moveset = _generate_moveset(cube.dimension)
    queue: list[MoveNode | None] = [None]

    while not is_solved(cube):
        current = queue.pop(0)

        for move in moveset:
            if isinstance(current, MoveNode) and move.face == current.move.face:
                continue

            new_node = MoveNode(move, current)
            queue.append(new_node)

            test_cube.reset()
            # test_cube.exec_alg(new_alg)
            _exec_movenodes(new_node, test_cube)

            if is_solved(test_cube):
                solution = _assemble_alg(new_node)
                print(f"Moves: {len(solution)}; Search space: {len(queue):,}")
                return solution

    print("Loop skipped")
    return []


def _generate_moveset(dimension: int) -> set[Move]:
    """
    Returns a set of all possible moves for a cube of the given dimension.
    No support for wide moves yet.
    """
    # typing needed to satisfy the type checker
    directions: list[Literal[-1, 1, 2]] = [-1, 1, 2]
    depth_range = range(1, (dimension // 2) + 1)

    combinations = product(Face, directions, depth_range)

    return {
        Move(face, direction, depth, False)
        for face, direction, depth in combinations
    }


# untested, may not be necessary
def _exec_movenodes(leaf: MoveNode, cube: Cube):
    """
    Travel up the leaf node passed in up to the parent node of its tree,
    executing every move on the passed in cube
    """
    node = leaf
    while node is not None:
        cube.move(node.move)
        node = node.parent


# untested, may not be necessary
def _assemble_alg(leaf: MoveNode) -> list[Move]:
    """
    Assemble an algorithm from a move tree, given a leaf node
    """
    alg = []
    node = leaf
    while node is not None:
        alg.append(node.move)
        node = node.parent

    return alg
