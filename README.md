# Cube Playground (WIP)
This is a Rubik's cube sandbox explorer built in Python for any NxNxN Rubik's cube.

## Current features:
- Rubik's cube generation of any size NxN, (2x2, 3x3, 100x100, as much as your CPU can handle)
- Algorithm execution (sequences of moves) via manual input
- Automatic scrambling
- Production of PNG images of any cube state

A barebones 3D visualization is currently functional, I am working on integrating the other features into the 3D window. To use the 3D window, press [S] to scramble the cube, [Space] to reset the cube, [Backspace] to undo a turn, and [U], [D], [F], [B], [L], [R] to perform the cooresponding turns on the cube. Holding [Shift] while doing so performs an inverted move (U', D', etc.).

## Requirements:
- Python 3.12
- [NumPy](https://pypi.org/project/numpy/)  (matrix operaitons)
- [Pillow](https://pypi.org/project/pillow/) (image generation)
- [Ursina](https://www.ursinaengine.org/) (3d graphics)

You can install these libraries through pip by running:
```
pip install -r src/requirements.txt
```
Once you have all the requirements installed, you can run the program by running:
```
python src/main.py
```

## Screenshots

<img src="./images/screenshots/3x3_3d.png" width="250"/>
<img src="./images/screenshots/3x3_flat.png" width="400"/>
<img src="./images/screenshots/20x20_3d.png" width="250"/>
<img src="./images/screenshots/2x2_flat.png" width="400"/>
