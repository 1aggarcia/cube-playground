# Cube Playground
Rubik's Cube playground in Python. I wrote the code in Spanish just to practice the language but the UI will be avaliable in English.

Presently, this codebase is capable of executing algorithms (sequences of moves), generating scrambles, and producing PNG images of Rubik's cubes of any size. These interactions can be done in the TKinter window opened by running `src/main.py`, but the initial cube is always a solved 3x3.

[NumPy](https://pypi.org/project/numpy/) and [Pillow](https://pypi.org/project/pillow/) are required to run this code, as well as Python 3.10ish

In the future, these features will be better integrated into the UI, including the ability to save cubes to open later and explore further. I'd like to implement an optimal solver, which will be slow (solving cubes optimally is an NP problem), as well as render cubes in 3D space instead of with TKinter. Maybe one day I'll even find a way to make a web client for it.
