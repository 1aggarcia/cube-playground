from copy import deepcopy
from ursina import Entity, Vec3

from constantes.enums import Cara
from constantes.colors import COLORES_DE_CUBO
from constantes.cubes import VECTORES_DE_CARA


class Cubito(Entity):
    """
    Modelo por un cubito de un cubo de Rubik en una aplicación Ursina.
    Debe usarse después de crear una aplicación Ursina.

    Tiene seis lados con colores distintos que se pueden colorar, y una
    posición mutable.
    """
    def __init__(self, x: float, y: float, z: float):
        super().__init__()

        self.position = Vec3(x, y, z)
        self._planos = {
            cara: _crear_plano(self, cara, COLORES_DE_CUBO[cara])
            for cara in Cara
        }

    @property
    def planos(self):
        return deepcopy(self._planos)

    def colorar(self, lado: Cara, color_hex: str):
        """
        Cambiar el color del lado especificado.

        - lado: El lado del cubito para cambiar el color
        - color_hex: El color nuevo, en hex
        """
        plano = self._planos[lado]
        plano.color_setter(color_hex)


def _crear_plano(raiz: Entity, cara: Cara, color: str):
    """
    Pegar un plano a un lado de la Entity dada

    - cara: El lado donde se pegará el plano
    - color: El color que tendrá el plano

    Retorna el plano nuevo
    """
    plano = Entity(
        parent = raiz,
        model = 'plane',
        texture = 'white_cube',
        color = color,
        origin_y = -0.5
    )
    plano.look_at(VECTORES_DE_CARA[cara], 'up')

    return plano
