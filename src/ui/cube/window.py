import tkinter as tk

from constants import colors
from models.cube import generate_cube
from ui.cube.draw_cube import create_cube_frame
from ui.cube.control_cube import create_control_frame


def create_cube_window(dimension: int):
    # configure window
    window = tk.Tk()
    window.config(bg=colors.GREEN_1)
    window.geometry('1100x600')

    # create and position widget
    central_frame = _create_central_frame(window, dimension)
    central_frame.place(relx=.5, rely=.5,anchor=tk.CENTER)

    return window


def _create_central_frame(root: tk.Misc, dimension: int):
    cubo = generate_cube(dimension)

    # create widgets
    frame = tk.Frame(root, padx=10, pady=10, bg=colors.GREEN_2)
    cube_frame = create_cube_frame(frame, cubo)
    control_frame = create_control_frame(frame, cubo)

    # positioning
    cube_frame.grid(row=0, column=0)
    control_frame.grid(row=0, column=1)

    return frame
