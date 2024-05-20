from ursina import EditorCamera, Ursina, Vec3, Entity
from models.cube3d import Cube3d
from models.move import Move, invert_move
from models.ursina_state import UrsinaState
from util.scrambles import generate_scramble
from util.printer import print_cube

from constants.enums import Face


CAMAERA_SCALE = 3


def init_ursina_app(dimension: int):
    app = Ursina()

    state = UrsinaState(Cube3d(dimension))

    scale = dimension / CAMAERA_SCALE
    camera = EditorCamera(ui_size = 1000)
    camera.scale_setter(Vec3(scale, scale, scale))

    controller = Entity()
    controller.input = lambda key: on_input(key, state)

    app.run()


# TODO: clean up state management
def on_input(key: str, state: UrsinaState):
    cube2d = state.cube.cube2d

    # execute correct task
    if key == "space":
        state.cube.cube2d.reset()
        state.history.clear()

    elif key == "s":
        scramble = generate_scramble(cube2d.dimension)
        cube2d.exec_alg(scramble)
        state.history.extend(scramble)

    elif key == "i":
        print_cube(cube2d)

    elif key == "backspace" and len(state.history) > 0:
        mov = state.history.pop()
        cube2d.move(invert_move(mov))

    elif key.upper() in Face:
        direction = -1 if "shift" in state.keys else 1
        mov = Move(Face[key.upper()], direction, 1, False)

        cube2d.move(mov)
        state.history.append(mov)

    # add key to set in state
    if " up" not in key:
        state.keys.add(key)
    elif key.strip(" up") in state.keys:
        state.keys.remove(key.strip(" up"))
