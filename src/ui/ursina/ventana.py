# Ursina nos fuerza a romper estas reglas
# pylint: disable=W0401
# pylint: disable=W0622
# pylint: disable=W0614

from ursina import *

from constantes.enums import Cara
from modelos.cubo3d import generar_cubo3d

VECTORES_DE_CARA = {
    Cara.U: Vec3(0, 1, 0),
    Cara.D: Vec3(0, -1, 0),
    Cara.F: Vec3(0, 0, -1),
    Cara.B: Vec3(0, 0, 1),
    Cara.L: Vec3(-1, 0, 0),
    Cara.R: Vec3(1, 0, 0)
}


def ventana_ursina(dimension: int):
    aplicacion = Ursina()

    cubo = generar_cubo3d(dimension)
    print(cubo.get_cubitos())

    EditorCamera()

    return aplicacion
