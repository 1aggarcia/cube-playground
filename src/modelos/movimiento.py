from typing import Literal
from constantes.enums import Cara

class Movimiento:
    """
    Objeto que define un movimiento del cubo. No se debería modificar.
    El movimiento es definido por:
    * cara - la cara que girará
    * direccion - número de rotaciones de 90 degrados de capa.
        Debe ser 1 por un movimiento en sentido horario, -1 por uno en
        sentido antihorario, o 2 para uno doble
    * nivel - cuantas capas de profundidad quieres girar. 1 es solo la cara.
        Debe ser menos de la dimension del cubo, más que 0
    * ancho - True si quieres girar cada capa entre la cara y el nivel,
        False si solo quieres girar la capa al nivel dado.
    """
    def __init__(self, cara: Cara, direccion: Literal[-1, 1, 2], nivel: int, ancho: bool):
        if nivel < 1:
            raise ValueError('nivel debe ser por lo menos 1')
        self.cara = cara
        self.direccion = direccion
        self.nivel = nivel
        self.ancho = ancho

    def __eq__(self, __value: object) -> bool:
        return (
            isinstance(__value, Movimiento)
            and self.cara == __value.cara
            and self.direccion == __value.direccion
            and self.ancho == __value.ancho
        )

    def __repr__(self):
        resultado = self.cara.value

        if self.ancho:
            # un movimiento ancho: U -> Uw
            resultado += 'w'

        if self.direccion == -1:
            # un movimiento primo: U -> U' o Uw -> Uw'
            resultado += "'"
        elif self.direccion == 2:
            # un movimiento doble: U -> U2 o Uw -> Uw2
            resultado += "2"

        if self.nivel > 1:
            # un movimiento de múltiples capas: U -> 3U o Uw' -> 3Uw' etc.
            resultado = str(self.nivel) + resultado

        return resultado


def invertir_movimiento(movimiento: Movimiento):
    """
    Retorna el mismo movimiento al revés, es decir, con la dirección invertida
    """
    if movimiento.direccion == 2:
        return movimiento

    return Movimiento(
        movimiento.cara,
        movimiento.direccion * -1, # type: ignore
        movimiento.nivel,
        movimiento.ancho
    )


def movimiento_de_texto(texto: str) -> Movimiento:
    """
    Convertir texto a un movimiento
    * requiere que el texto tenga una letra que represente una cara,
        e.j. <U>
    * requiere que el nivel esté antes de la cara, e.j. <3U>
    * requiere que el carácter <w> aparezca después de la cara si
        el movimiento es ancho, e.j. <Uw>
    * requiere que la dirección sea indicada por <'> para prima o <2> para
        double, al fin del movimiento, e.j. <U'>, <Uw2>, <3Dw'>
    """
    length = len(texto)

    if length < 1:
        raise ValueError('texto está vacío')
    i = 0

    # determinar nivel (opcional)
    nivel = 1
    while texto[i].isdigit() and i < length:
        i += 1
    if i != 0:
        nivel = int(texto[0:i])

    # determinar cara (obligatorio)
    if i >= length:
        raise ValueError('El texto no contiene una cara')
    cara = Cara[texto[i]]
    i += 1

    # determinar ancho (opcional)
    ancho = False
    if i >= length:
        return Movimiento(cara, 1, nivel, False)
    if texto[i] == 'w':
        ancho = True
        i += 1

    # determinal dirección (opcional)
    if i >= length:
        return Movimiento(cara, 1, nivel, ancho)
    if texto[i] == "'":
        return Movimiento(cara, -1, nivel, ancho)
    if texto[i] == '2':
        return Movimiento(cara, 2, nivel, ancho)

    # hay uno o más carácters que no tienen nada que ver con un movimiento
    raise ValueError(f'Carácter ilegal en movimiento: {texto[i]}')
