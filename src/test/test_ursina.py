# disable private method access warning
# pylint: disable=W0212

import unittest
from ursina import Ursina

from ui.ursina import app
from models.cube import generate_cube
from models.cube3d import Cube3d
from models.move import text_to_move
from models.ursina_state import UrsinaState

class TestUrsina(unittest.TestCase):
    def test_on_input(self):
        Ursina(window_type='none')

        state = UrsinaState(Cube3d(3))
        model_cube = generate_cube(3)

        def _assert_state():
            self.assertEqual(model_cube, state.cube.cube2d)

        # basic moves
        app.on_input("u", state)
        model_cube.move(text_to_move("U"))
        _assert_state()

        app.on_input("d", state)
        app.on_input("b", state)
        app.on_input("d", state)
        app.on_input("f", state)
        model_cube.move(text_to_move("D"))
        model_cube.move(text_to_move("B"))
        model_cube.move(text_to_move("D"))
        model_cube.move(text_to_move("F"))
        _assert_state()

        # irrelevant keys
        app.on_input("d up", state)
        _assert_state()

        app.on_input("u hold", state)
        app.on_input("t", state)
        _assert_state()

        # reset
        app.on_input("space", state)
        model_cube.reset()
        _assert_state()

        # scamble
        app.on_input("s", state)
        self.assertNotEqual(model_cube, state.cube.cube2d)
