from dataclasses import dataclass, field

from models.cube3d import Cube3d
from models.move import Move


@dataclass(frozen=True)
class UrsinaState:
    """
    Fields comprising the state of our Ursina app

    - cube: The app's Cube3d model
    - keys: The keys that have been pressed
    - history: Stack of moves executed on the cube

    """
    cube: Cube3d
    keys: set[str] = field(default_factory=set)
    history: list[Move] = field(default_factory=list)
