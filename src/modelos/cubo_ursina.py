from ursina import Entity, Vec3

from constantes.enums import Cara
from constantes.colores import COLORES_DE_CUBO

VECTORES_DE_CARA = {
    Cara.U: Vec3(0, 1, 0),
    Cara.D: Vec3(0, -1, 0),
    Cara.F: Vec3(0, 0, -1),
    Cara.B: Vec3(0, 0, 1),
    Cara.L: Vec3(-1, 0, 0),
    Cara.R: Vec3(1, 0, 0)
}


class Cubito(Entity):
    def __init__(self):
        super().__init__()

        # valores por defecto
        self.position = Vec3(0, 0, 0)
        for cara in Cara:
            _crear_plano(self, cara, cara)

    def pos(self, x: float, y: float, z: float):
        self.position = Vec3(x, y, z)
        return self


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
