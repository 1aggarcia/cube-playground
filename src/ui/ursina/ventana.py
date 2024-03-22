# Ursina nos fuerza a romper estas reglas
# pylint: disable=W0401
# pylint: disable=W0622
# pylint: disable=W0614

from ursina import *

from constantes.enums import Cara
from constantes.colores import COLORES_DE_CUBO
# from modelos.cubo import generar_cubo

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

    _generar_cubitos(dimension)

    cubito = Entity(scale=3)

    _crear_plano(cubito, Cara.F, Cara.F)
    _crear_plano(cubito, Cara.B, Cara.B)

    _crear_plano(cubito, Cara.U, Cara.U)
    _crear_plano(cubito, Cara.D, Cara.D)

    _crear_plano(cubito, Cara.L, Cara.L)
    _crear_plano(cubito, Cara.R, Cara.R)

    EditorCamera()

    return aplicacion


def _generar_cubitos(dimension: int):
    desviacion = -(dimension - 1) / 2

    for capa in range(dimension):
        for columna in range(dimension):
            for fila in range(dimension):
                x = desviacion + fila
                y = desviacion + columna
                z = desviacion + capa

                if (
                    0 < capa < dimension - 1
                    and 0 < columna < dimension - 1
                    and 0 < fila < dimension - 1
                ):
                    continue

                cara_arbitraria = random.choice(list(Cara))
                cubito = Cubito(cara_arbitraria)
                cubito.pos(x, y, z)


def _crear_plano(raiz: Entity, cara: Cara, tono: Cara):
    plano = Entity(
        parent = raiz,
        model = 'plane',
        texture = 'white_cube',
        color = COLORES_DE_CUBO[tono],
        origin_y = -0.5
    )
    plano.look_at(VECTORES_DE_CARA[cara], 'up')

    return plano


class Cubito(Entity):
    def __init__(self, cara: Cara):
        super().__init__()
        self.color = COLORES_DE_CUBO[cara]

        # valores por defecto
        self.position = Vec3(0, 0, 0)
        self.model = 'cube'
        self.texture = 'white_cube'

    def pos(self, x: float, y: float, z: float):
        self.position = Vec3(x, y, z)
        return self

    # def update(self):
    #     self.rotation_x += 1
    #     self.rotation_y -= 1

    def input(self, key: str):
        if key == 'd':
            self.x += 1
        elif key == 'a':
            self.x -= 1
        elif key == 'w':
            self.y += 1
        elif key == 's':
            self.y -= 1
