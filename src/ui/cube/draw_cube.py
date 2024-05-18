import tkinter as tk

from models.cube import Cube
from constants import colors
from constants.enums import Face

FACE_SIZE = 160 # width and height of a face


def create_cube_frame(root: tk.Misc, cube: Cube):
    frame = tk.Frame(root, bg=colors.GREEN_2, padx=10)

    # create widgets for each face
    face_u = _create_face_frame(frame, cube, Face.U)
    face_l = _create_face_frame(frame, cube, Face.L)
    face_f = _create_face_frame(frame, cube, Face.F)
    face_r = _create_face_frame(frame, cube, Face.R)
    face_b = _create_face_frame(frame, cube, Face.B)
    face_d = _create_face_frame(frame, cube, Face.D)

    # position the frames so that they form a flat cube
    face_u.grid(row=0, column=1)
    face_l.grid(row=1, column=0)
    face_f.grid(row=1, column=1)
    face_r.grid(row=1, column=2)
    face_b.grid(row=1, column=3)
    face_d.grid(row=2, column=1)

    cube.on_change(lambda: _color_cube(frame, cube))

    return frame


def _color_cube(frame: tk.Frame, cube: Cube) -> None:
    """
    Color the given frame with the given cube
    * requires that the frame have 6 children with names 'u', 'd', 'l', 'r', 'f', 'b'
    * requires that each child of the frame is a frame with NxN children that
        are frames, where N = cube.dimension
    
    *  modified the given frame, changes the color of each piece
    """
    for face in list(Face):
        # check requirement 1
        try:
            square = frame.nametowidget(face.value.lower())
            # helper function checks requirement 2
            _color_face(square, cube, face)
        except KeyError as exc:
            raise ValueError(
                'BROKEN REQUIREMENT: frame children have incorrect names'
            ) from exc

    # looks better when theres a short pause
    # between each movement of an algorithm
    frame.update()


def _create_face_frame(root: tk.Misc, cube: Cube, face: Face) -> tk.Frame:
    """
    Creates a frame representing the given face with a matrix of NxN pieces,
    where N = len(face) indicated. It is colored according to the given cube

    * returns a new frame with the name of `face` in lowercase, with NxN
        colored children of equal size
    """
    # calculate size of the pieces to fit all of them in a frame
    dimension = cube.dimension
    piece_size = int(FACE_SIZE / dimension)

    # create central frame
    frame = tk.Frame(root, bg='black', name=face.value.lower(),
                    width=FACE_SIZE, height=FACE_SIZE,
                    borderwidth=2)

    # fill frame with pieces
    for i in range(dimension):
        for j in range(dimension):
            piece_frame = tk.Frame(
                frame,
                width=piece_size,
                height=piece_size,
                borderwidth=1,
                relief=tk.RAISED,
            )
            # position the frame accorting to the source matrtix
            piece_frame.grid(row=i, column=j)

    # color the frame before returing
    _color_face(frame, cube, face)
    return frame


def _color_face(frame: tk.Frame, cube: Cube, face: Face) -> None:
    """
    Color the frame given with the cube and face given
    * requires that the frame have NxN children frames, where N = cube.dimension
    * modifies the given frame, coloring its pieces
    """
    dimension = cube.dimension
    children = frame.winfo_children()
    if len(children) != dimension**2:
        raise ValueError('BROKEN REQUIREMENT: frame does not have NxN children')

    square = cube.get_face(face)

    for i in range(dimension):
        for j in range(dimension):
            # flatten 2D faces to 1D children
            # piece [i][j] in 2D is equivelant to [i * dimension + j] in 1D
            piece = children[i*dimension + j]
            color = colors.CUBE_COLORS[square[i][j]]
            # the modification
            piece.configure(bg = color) # type: ignore
