from ursina import Vec3
from models.cube import cube_from_str
from constants.enums import Face


FACE_VECTORS = {
    Face.U: Vec3(0, 1, 0),
    Face.D: Vec3(0, -1, 0),
    Face.F: Vec3(0, 0, -1),
    Face.B: Vec3(0, 0, 1),
    Face.L: Vec3(-1, 0, 0),
    Face.R: Vec3(1, 0, 0)
}


MY_CUBE = cube_from_str(
     u= [['U', 'D'],
        ['U', 'U']],

     d= [['R', 'D'],
        ['D', 'L']],

     f= [['F', 'F'],
        ['B', 'R']],

     b= [['F', 'B'],
        ['D', 'B']],

     l= [['L', 'L'],
        ['L', 'U']],

     r= [['R', 'R'],
        ['B', 'F']]
)


SUPERFLIP = cube_from_str(
     u= [['U', 'B', 'U'],
         ['L', 'U', 'R'],
         ['U', 'F', 'U']],

     d= [['D', 'F', 'D'],
         ['L', 'D', 'R'],
         ['D', 'B', 'D']],

     f= [['F', 'U', 'F'],
         ['L', 'F', 'R'],
         ['F', 'D', 'F']],

     b= [['B', 'U', 'B'],
         ['R', 'B', 'L'],
         ['B', 'D', 'B']],

     l= [['L', 'U', 'L'],
         ['B', 'L', 'F'],
         ['L', 'D', 'L']],

     r= [['R', 'U', 'R'],
         ['F', 'R', 'B'],
         ['R', 'D', 'R']],
)


BAD_CORNER = cube_from_str(
     u= [['U', 'U', 'U'],
         ['U', 'U', 'U'],
         ['U', 'U', 'F']],

     d= [['D', 'D', 'D'],
         ['D', 'D', 'D'],
         ['D', 'D', 'D']],

     f= [['F', 'F', 'R'],
         ['F', 'F', 'F'],
         ['F', 'F', 'F']],

     b= [['B', 'B', 'B'],
         ['B', 'B', 'B'],
         ['B', 'B', 'B']],

     l= [['L', 'L', 'L'],
         ['L', 'L', 'L'],
         ['L', 'L', 'L']],

     r= [['U', 'R', 'R'],
         ['R', 'R', 'R'],
         ['R', 'R', 'R']],
)
