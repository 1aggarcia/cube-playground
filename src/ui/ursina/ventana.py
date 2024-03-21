# Ursina fuerza a romper estas reglas
# pylint: disable=W0401
# pylint: disable=W0622
# pylint: disable=W0614

from ursina import *

from constantes.enums import Cara
from constantes.colores import COLORES_DE_CUBO
# from modelos.cubo import generar_cubo


def ventana_ursina(dimension: int):
    aplicacion = Ursina()

    # cubo = generar_cubo(dimension)
    desviacion = -(dimension - 1) / 2

    for capa in range(dimension):
        for columna in range(dimension):
            for fila in range(dimension):
                cara_arbitraria = random.choice(list(Cara))
                cubito = Cubito(cara_arbitraria)
                cubito.pos(
                    desviacion + fila,
                    desviacion + columna,
                    desviacion + capa
                )

    EditorCamera()

    return aplicacion


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
