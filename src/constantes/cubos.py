from ursina import Vec3
from modelos.cubo import crear_cubo_de_texto
from constantes.enums import Cara


VECTORES_DE_CARA = {
    Cara.U: Vec3(0, 1, 0),
    Cara.D: Vec3(0, -1, 0),
    Cara.F: Vec3(0, 0, -1),
    Cara.B: Vec3(0, 0, 1),
    Cara.L: Vec3(-1, 0, 0),
    Cara.R: Vec3(1, 0, 0)
}


MI_CUBO = crear_cubo_de_texto(
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


SUPERFLIP = crear_cubo_de_texto(
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


ESQUINA_MALA = crear_cubo_de_texto(
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
