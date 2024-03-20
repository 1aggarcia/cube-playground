from ursina import *
from constantes.enums import Cara
from constantes.colores import COLORES_DE_CUBO

def ventana_ursina():
    aplicacion = Ursina()

    cubo = Entity(model='cube', texture='white_cube')
    cubo.color = COLORES_DE_CUBO[Cara.L]
    cubo.update = lambda: update_cubo(cubo)
    cubo.input = lambda key: move_cubo(cubo, key)

    return aplicacion

def update_cubo(cubo: Entity):
    cubo.rotation_x += 1
    cubo.rotation_y += 0.6

def move_cubo(cubo: Entity, key: str):
    if key == 'd':
        cubo.x += 1
    elif key == 'a':
        cubo.x -= 1
    elif key == 'w':
        cubo.y += 1
    elif key == 's':
        cubo.y -= 1
