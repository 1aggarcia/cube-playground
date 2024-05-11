from dataclasses import dataclass, field

from modelos.cubo3d import Cubo3d
from modelos.movimiento import Movimiento


@dataclass(frozen=True)
class EstadoUrsina:
    """
    Conjunto de campos del estado de una app Ursina

    - cubo: El Cubo3d de la app
    - teclas: Las teclas que han sido presionadas
    - historial: Una pila de los movimientos realizados en el cubo
    """
    cubo: Cubo3d
    teclas: set[str] = field(default_factory=set)
    historial: list[Movimiento] = field(default_factory=list)
