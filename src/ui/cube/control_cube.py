import tkinter as tk
from tkinter import messagebox
import time

import models.move as mv
from models.cube import Cube
from util.solver import find_optimal_solution
from util.scrambles import generate_scramble
from util.printer import print_cube
from constants import colors

PADDING = 10


class CubeController:
    """
    Bind cube state and its history to the TKinter widgets in the open window
    so that they can be modified together
    """
    def __init__(self,
        cube: Cube, input_box: tk.Entry, history: tk.Text
    ):
        self._cube = cube
        self._input_box = input_box
        self._history_widget = history
        self._history = []

    def apply_alg(self):
        text = self._input_box.get()
        alg = text.split(' ')
        try:
            self._cube.exec_str_alg(alg)
        except (ValueError, KeyError) as e:
            messagebox.showerror('Error', f'Error: {e}')
            return

        self._input_box.delete(0, tk.END)
        self._history.extend(alg)
        self._update_history()

    def undo(self):
        if len(self._history) == 0:
            return

        mov = mv.text_to_move(self._history.pop())
        self._update_history()
        inverted = mv.invert_move(mov)
        self._cube.move(inverted)

    def print_cube(self):
        print_cube(self._cube)

    def invert(self):
        text = self._input_box.get()
        try:
            alg = [mv.text_to_move(mov) for mov in text.split(' ')]
        except (ValueError, KeyError) as e:
            messagebox.showerror('Error', f'Error: {e}')
            return

        inverted_alg = [mv.invert_move(mov) for mov in alg]
        inverted_alg.reverse()

        inverted_text = [str(mov) for mov in inverted_alg]

        self._input_box.delete(0, tk.END)
        self._input_box.insert(0, ' '.join(inverted_text))

    def scramble_cube(self):
        scramble = generate_scramble(self._cube.dimension)

        self._history.extend([str(mov) for mov in scramble])
        self._update_history()
        self._cube.exec_alg(scramble)

    def reset_cube(self):
        self._cube.reset()
        self._history.clear()
        self._update_history()

    def solve_cube(self):
        start = time.perf_counter()
        sol = find_optimal_solution(self._cube)
        end = time.perf_counter()
        print(f"* exec time: {end - start}")
        str_scramble = ' '.join([str(mov) for mov in sol])

        messagebox.showinfo(message=str_scramble)

    def _update_history(self):
        self._history_widget.delete(1.0, tk.END)
        self._history_widget.insert(tk.END, ' '.join(self._history))


def create_control_frame(raiz: tk.Misc, cubo: Cube):
    """
    Returns a new control frame for the TKinter cube window
    """
    frame = tk.Frame(raiz, bg=colors.GREEN_2)

    history = tk.Text(frame, width=30, height=10)
    input_box = tk.Entry(frame, width=30)

    history.pack()
    input_box.pack()

    controller = CubeController(cubo, input_box, history)

    button_frame = _create_button_frame(frame, controller)
    button_frame.pack()

    return frame


def _create_button_frame(root: tk.Misc, controller: CubeController):
    """
    Return a new buttom frame to controll the window's cube
    """
    frame = tk.Frame(root, padx=PADDING, pady=PADDING)

    # create buttons
    apply_btn = tk.Button(
        frame, text='Apply Algorithm', command=controller.apply_alg
    )
    undo_btn = tk.Button(
        frame, text='Undo last move', command=controller.undo
    )
    invert_btn = tk.Button(
        frame, text='Invert Algorithm', command=controller.invert
    )
    scramble_btn = tk.Button(
        frame, text='Scramble', command=controller.scramble_cube
    )
    image_btn = tk.Button(
        frame, text='Export PNG', command=controller.print_cube
    )
    reset_btn = tk.Button(
        frame, text='Reset Cube State', command=controller.reset_cube
    )
    solve_btn = tk.Button(
        frame, text='Find Optimal Solution', command=controller.solve_cube
    )

    # position them
    apply_btn.grid(row=0, column=0)
    undo_btn.grid(row=0, column=1)

    invert_btn.grid(row=1, column=0)
    scramble_btn.grid(row=1, column=1)


    image_btn.grid(row=2, column=0)
    reset_btn.grid(row=2, column=1)

    solve_btn.grid(row=3, column=0)

    return frame
