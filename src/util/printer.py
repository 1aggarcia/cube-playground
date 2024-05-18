from datetime import datetime
from PIL import Image, ImageDraw

from constants.enums import Face
from constants import colors
from models.cube import Cube

SAVE_PATH = '../images/generated'

# which positions the faces begin at
OFFSETS_X = {
    Face.U: 1, Face.D: 1, Face.F: 1, Face.B: 3, Face.R: 2, Face.L: 0
}
OFFSETS_Y = {
    Face.U: 0, Face.D: 2, Face.F: 1, Face.B: 1, Face.R: 1, Face.L: 1
}

# size of a sticker block
BLOCK = 50

PADDING = 2

# the number of blocks in that the image takes up
WIDTH = 4
HEIGHT = 3

def print_cube(cube: Cube):
    """
    Given a cube, produce a PNG image with the cube state in 2D.
    The file will have the name "cubo_{n}x{x}_{YYYYMMDD}_{HHMMSS}.png",
    for example: "cube_3x3_20240518_100452.png"
    """
    dim = cube.dimension
    width = PADDING + (dim * WIDTH)
    height = PADDING + (dim * HEIGHT)

    width_px = width * BLOCK
    height_px = height * BLOCK

    # create image
    imagen = Image.new('RGB', (width_px, height_px), colors.YELLOW_1)

    # draw cube into the image
    for face in Face:
        offset_x = OFFSETS_X[face] * dim + 1
        offset_y = OFFSETS_Y[face] * dim + 1
        _draw_face(imagen, cube, face, (offset_x, offset_y))

    # save image
    name = f'{SAVE_PATH}/cube_{dim}x{dim}_{timestamp()}.png'
    imagen.save(name)
    imagen.show()


def _draw_face(
        image: Image.Image, cube: Cube, face: Face, offset: tuple[int, int]
    ):
    """
    In the given image, draw the face indicated of the cube given
    starting at the blocks indicated by the offset
    - offset must have the form (offset_x, offset_y)
    """
    square = cube.get_face(face)

    for y, row in enumerate(square):
        for x, piece in enumerate(row):
            color = colors.CUBE_COLORS[piece]
            offset_x = offset[0] + x
            offset_y = offset[1] + y
            _draw_block(image, offset_x, offset_y, color)


def _draw_block(image: Image.Image, x: int, y: int, color):
    """
    In the given image, draw a block at position (x, y) with the given color
    """
    start = (x * BLOCK, y * BLOCK)
    end = ((x+1) * BLOCK, (y+1) * BLOCK)

    draw = ImageDraw.Draw(image)
    draw.rectangle((start, end), fill=color, outline='black', width=2)


def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")
