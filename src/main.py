import tkinter as tk
from tkinter import messagebox

from constants import colors
from constants.enums import Window
from ui.cube.window import create_cube_window
from ui.ursina.app import init_ursina_app


def welcome_window():
    window = tk.Tk()
    window.config(bg=colors.GREEN_1)
    window.geometry('300x200')
    window.eval('tk::PlaceWindow . center')

    dim_label = tk.Label(window, text='Dimension:', bg=colors.GREEN_1)
    dim_entry = tk.Entry(window)

    dim_entry.insert(0, '3')

    def local_open(destination: Window):
        dimension = dim_entry.get()
        if dimension.isdigit() is False:
            messagebox.showerror('Error', 'Dimension is not a number')
            return

        if int(dimension) < 2:
            messagebox.showerror('Error', f'Dimension is less than 2: {dimension}')
            return

        window.destroy()
        open_window(destination, int(dimension))

    cube_btn = tk.Button(window, text='Open new cube',
                            command=lambda: local_open(Window.CUBO))
    ursina_btn = tk.Button(window, text='Open in 3D (Beta)',
                            command=lambda: local_open(Window.URSINA))

    dim_label.grid(row=0, column=0)
    dim_entry.grid(row=0, column=1)

    cube_btn.grid(row=1, column=0)
    #.place(relx=0.25, rely=0.66, anchor=tk.CENTER)
    ursina_btn.grid(row=1, column=1)
    #.place(relx=0.75, rely=0.66, anchor=tk.CENTER)

    return window


def open_window(destination: Window, dimension: int):
    if destination == Window.URSINA:
        init_ursina_app(dimension)
    else:
        create_cube_window(dimension).mainloop()


if __name__=="__main__":
    welcome_window().mainloop()

# RUN TESTS
# $ python3 -m unittest -v
# $ pylint --disable=C0114,C0115,C0116,W0511,R0913,R0801 $(git ls-files '*.py')
# from /src/

# TODO: improve scrambling algorithm
# TODO: implement wide moves (w)
# TODO: validate cubes / move construction to constructor
# TODO: improve conservion of text -> algorithm
# TODO: remove cube.py:121
# TODO: test_cube3d.py - start Ursina app
