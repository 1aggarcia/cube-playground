from typing import Literal
from dataclasses import dataclass
from constants.enums import Face


@dataclass(frozen=True)
class Move:
    """
    Immutable model of a Rubik's cube move. Is is defined by:

    - face: The face to turn on the cube
    - direction: number of 90 degree rotations on the layer.
        * Should be 1 for a clockwise turn, -1 for a counterclockwise turn
        * Should be 2 for a 180 degree turn
    - depth: How many layers deep the cube should be turned.
        Must be between 1 - cube dimension
    - is_wide: True if every layer between the depth layer and surface layer
        should be turned, False if only the depth layer should be turned
    """
    face: Face
    direction: Literal[-1, 1, 2]
    depth: int
    is_wide: bool

    def __repr__(self):
        result = self.face.value

        if self.is_wide:
            # wide turn: U -> Uw
            result += 'w'

        if self.direction == -1:
            # Inverted turn: U -> U' or Uw -> Uw'
            result += "'"
        elif self.direction == 2:
            # double turn: U -> U2 or Uw -> Uw2
            result += "2"

        if self.depth > 1:
            # U -> 3U or Uw' -> 3Uw' etc.
            result = str(self.depth) + result

        return result


def invert_move(move: Move):
    """
    Return the same move, but with the direction reversed
    """
    if move.direction == 2:
        return move

    return Move(
        move.face,
        move.direction * -1,
        move.depth,
        move.is_wide
    )


def text_to_move(text: str) -> Move:
    """
    Convert a string to a move

    * requires that the text have a letter representing a face, e.g. <U>
    * requires the depth to be before the face, e.g. <3U>
    * requires that the character <w> appear after the face, if wide move.
        e.g. <Uw>
    * requires the direction to be indicated by <'> for prime or <2> for
        double, at the end of the move, e.g. <U'>, <Uw2>, <3Dw'>
    
    Returns a move interpreted from `text`
    """
    length = len(text)

    if length < 1:
        raise ValueError('text is empty')
    pos = 0

    # determine depth (optional)
    depth = 1
    while text[pos].isdigit() and pos < length:
        pos += 1
    if pos != 0:
        depth = int(text[0:pos])

    # determine face (mandatory)
    if pos >= length:
        raise ValueError('Passed in text has no face')
    cara = Face[text[pos]]
    pos += 1

    # determine if the move is wide (optional)
    wide = False
    if pos >= length:
        return Move(cara, 1, depth, False)
    if text[pos] == 'w':
        wide = True
        pos += 1

    # determine direction (optional)
    if pos >= length:
        return Move(cara, 1, depth, wide)
    if text[pos] == "'":
        return Move(cara, -1, depth, wide)
    if text[pos] == '2':
        return Move(cara, 2, depth, wide)

    # there are one of more characteres that have nothing to do with the move
    raise ValueError(f'Illegal character in passed in text: {text[pos]}')
